const date_pattern = /^((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/((?:19|20)\d{2}) (0?[1-9]|1[012])(:[0-5]\d) [APap][mM]$/;

$(function () {
    $('#appointment-datetime-group').datetimepicker({
        format: 'DD/MM/YYYY hh:mm A',
        minDate: moment(),
        daysOfWeekDisabled: [0, 6],
        stepping: 5
    });
});

let validate_appointment_form = function(form, type_select, location_select, date_time_input) {
    is_valid = true;

    let type_validator = $(form).find('#appointment-type-validator');
    if ($(type_select).children("option:selected").val() != "default") {
        $(type_validator).html('Looks good!');
        $(type_select).attr('class', 'custom-select form-control is-valid');
        $(type_validator).attr('class', 'valid-feedback')
    } else {
        $(type_validator).html('Please select the appointment\'s type.');
        $(type_select).attr('class', 'custom-select form-control is-invalid');
        $(type_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    let location_validator = $(form).find('#appointment-location-validator');
    if ($(location_select).children("option:selected").val() != "default") {
        $(location_validator).html('Looks good!')
        $(location_select).attr('class', 'custom-select form-control is-valid');
        $(location_validator).attr('class', 'valid-feedback')
    } else {
        $(location_validator).html('Please select the appointment\'s location.');
        $(location_validator).attr('class', 'invalid-feedback d-block');
        $(location_select).attr('class', 'custom-select form-control is-invalid');
        is_valid = false;
    }

    let date_validator = $(form).find('#appointment-date-validator');
    if (date_time_input.val().match(date_pattern) != null) {
        $(date_validator).html('Looks good!');
        $(date_time_input).attr('class', 'form-control datetimepicker-input is-valid');
        $(date_validator).attr('class', 'valid-feedback');
    } else {
        $(date_validator).html('Please select a valid date!');
        $(date_time_input).attr('class', 'form-control datetimepicker-input is-invalid');
        $(date_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    return is_valid;
}

let close_appointment_form = function() {
    let form = $('#appointment-form');

    let appointment_reason_select = $(form).find('#appointment-type');
    let type_validator = $(form).find('#appointment-type-validator');
    $(type_validator).html('')
    $(appointment_reason_select).attr('class', 'custom-select form-control');

    let appointment_location_select = $(form).find('#appointment-location');
    let location_validator = $(form).find('#appointment-location-validator');
    $(location_validator).html('');
    $(appointment_location_select).attr('class', 'custom-select form-control');

    let appointment_datetime_input = $(form).find('#appointment-datetime');
    let date_validator = $(form).find('#appointment-date-validator');
    $(date_validator).html('');
    $(appointment_datetime_input).attr('class', 'form-control datetimepicker-input');


    //HACK: unset global variable
    current_appointment_patient = null;

    appointment_loaded(form);
    $('#new-appointment-model').modal('hide');
    $(form).attr('class', '');
    $(form).trigger('reset');
}

let create_appointment = function (patient) {
    return function () {
        
        // HACK: set global variable with patient
        current_appointment_patient = patient;

        let form = $("#appointment-form");
        
        let forename_input = $(form).find('#appointment-forename');
        forename_input.val(patient.user_forename);

        let surname_input = $(form).find('#appointment-surname');
        surname_input.val(patient.user_surname);

        let dob_input = $(form).find('#appointment-dob');
        dob_input.val(patient.user_dob);

        let email_input = $(form).find('#appointment-email');
        email_input.val(patient.user_email);

        let location_select = $(form).find('#appointment-location');
        $(location_select).find('option').not(':first').remove();

        for (let i = 0; i < context_manager._cache.locations.length; i++) {
            let location = context_manager._cache.locations[i];

            let option = document.createElement('option');
            $(option).val(`${location.location_id}`);
            $(option).text(`${location.location_name}, ${location.location_address}, ${location.location_postcode}, ${location.location_city}`);
            $(location_select).append(option);
        }
    }
}

let appointment_loading = function(form) {
    let cancel_submit = $(form).find('#cancel-appointment');
    let submit = $(form).find('#submit-appointment');

    let spinner_markdown = `<span id="appointment-sending-spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Creating...`;
    $(submit).html(spinner_markdown);

    $(cancel_submit).prop('disabled', true);
    $(submit).prop('disabled', true);
}

let appointment_loaded = function(form) {
    let cancel_submit = $(form).find('#cancel-appointment');
    let submit = $(form).find('#submit-appointment');

    $(submit).html("Create Appointment");

    $(cancel_submit).prop('disabled', false);
    $(submit).prop('disabled', false);
}

let handle_appointment_success = function(appointment) {
    let patient_id = appointment.created_for;

    if (context_manager._cache.online_users[`${patient_id}`] != undefined) {
        // Patient is online, notify them that they have an appointment.
        socket.emit('notify_patient', {'data': {'appointment': appointment}, 'room_id': context_manager._cache.online_users[`${patient_id}`]});
    }

    // Add the appointment to the context
    context_manager._cache.appointments.push(appointment);

    // Update the patient component
    let appointment_count = $(`#patient_appointment_count_${appointment.created_for}`);
    $(appointment_count).html(Number($(appointment_count).html()) + 1);

    context_manager.success_message(`Your appointment has successfully been scheduled for ${moment(appointment.appointment_date_utc).format('dddd Do MMM YYYY')}`)
}

let submit_appointment = function(form) {
    try {
    
        let appointment_reason_select = $(form).find('#appointment-type');
        let appointment_location_select = $(form).find('#appointment-location');
        let appointment_datetime_input = $(form).find('#appointment-datetime');
        let appointment_notes_input = $(form).find('#appointment-notes');

        if (validate_appointment_form(form, appointment_reason_select, appointment_location_select, appointment_datetime_input)) {
            
            appointment_loading(form);

            let appointment = {
                    "appointment_id": context_manager.new_guid(),
                    "created_by": context_manager._cache.settings.user.user_id,
                    "created_for": current_appointment_patient.user_id,
                    "location_id": $(appointment_location_select).children("option:selected").val(),
                    "created_on_utc": moment().utc().format(),
                    "appointment_date_utc": moment(appointment_datetime_input.val(), "DD/MM/YYYY hh:mm A").utc().format(),
                    "appointment_type": $(appointment_reason_select).children("option:selected").text(),
                    "appointment_notes": appointment_notes_input.val(),
                    "is_cancelled": false,
                    "is_attended": false
            };

            $.ajax({
                url: `http://${context_manager._cache.configurations['host']}:${context_manager._cache.configurations['port']}/api/v1.0/appointments/`,
                type: 'POST',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
                },
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(appointment),
                success: function() {
                    handle_appointment_success(appointment);
                    close_appointment_form();
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENT', errorThrown);
                    context_manager.error_message(`Your appointment for ${current_appointment_patient.user_forename} ${current_appointment_patient.user_surname} couldn't be created. Please try again.`);

                    appointment_loaded(form);
                }
            })
        }
    } catch (err) {
        context_manager.post_exception('post_exception', err);
        context_manager.error_message(`An unexpected error has occurred whilst creating your appointment, please try again.`);

        appointment_loaded(form);
    }
}

let build_appointment = function(appointment_json) {
    try {
        console.log("Build clinician appointment...")
    } catch (err) {
        console.log(`An error has occurred whilst building an appointment element. ${err}`)
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENTS', err)
    }
}

