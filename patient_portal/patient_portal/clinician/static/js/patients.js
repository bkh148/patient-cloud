let edit_patient = function (patient) {
    context_manager.post_activity('SCRIPT_PATIENT_CLINICIAN_EDIT_PATIENT_CLICKED');
    context_manager.info_message("The ability to edit patients data will be added in a feature version of Patient Portal.");
}

let transfer_patient = function (patient) {
    context_manager.post_activity('SCRIPT_PATIENT_CLINICIAN_TRANSFER_PATIENT_CLICKED');
    context_manager.info_message("The ability to transfer patients will be added in a feature version of Patient Portal.");
}

let update_status_badge = function (user_id, status) {
    let status_badge = $(`#status-badge_${user_id}`);
    $(status_badge).attr('class', `badge-status badge-${status}`);
}

let upcoming_appointments_count = function (patient) {
    let count = 0;
    context_manager._cache.appointments.forEach(function (appointment) {
        if (appointment.created_for == patient.user_id && moment(appointment.appointment_date_utc) > moment()) {
            count++;
        }
    });

    return count;
}

let build_patient = function (patient) {
    try {
        let patient_wrapper = document.createElement('div');
        patient_wrapper.setAttribute('id', `patient_wrapper_${patient.user_id}`);
        patient_wrapper.innerHTML = context_manager._cache.templates['patient_item']

        /************ HEADER   ***********/
        // Get / Set the patients name in the header
        let patient_name = $(patient_wrapper).find('#patient_name');
        $(patient_name).attr('id', `${patient_name.attr('id')}_${patient.user_id}`);
        $(patient_name).html(`${context_manager.format_name(patient.user_surname)}, ${context_manager.format_name(patient.user_forename)}`);

        // Status badge
        let patient_badge = $(patient_wrapper).find('#status-badge');
        $(patient_badge).attr('id', `${patient_badge.attr('id')}_${patient.user_id}`);

        if (context_manager._cache.online_users[`${patient.user_id}`] !== undefined) {
            $(patient_badge).addClass('badge-online');
        } else {
            $(patient_badge).addClass('badge-offline');
        }

        // New appointment button
        let new_appointment_button = $(patient_wrapper).find('#new-appointment');
        $(new_appointment_button).attr('id', `${new_appointment_button.attr('id')}_${patient.user_id}`);
        $(new_appointment_button).on('click', function () {
            create_appointment(patient);
        });

        // Edit user button
        let edit_patient_button = $(patient_wrapper).find('#edit-patient');
        $(edit_patient_button).attr('id', `${edit_patient_button.attr('id')}_${patient.user_id}`);
        $(edit_patient_button).on('click', function () {
            edit_patient(patient)
        });

        // Transfer of care button
        let transfer_of_care = $(patient_wrapper).find('#transfer-patient');
        $(transfer_of_care).attr('id', `${transfer_of_care.attr('id')}_${patient.user_id}`);
        $(transfer_of_care).on('click', function () {
            transfer_patient(patient)
        });


        /************ BODY  ***********/
        let patient_id = $(patient_wrapper).find('#patient_id');
        $(patient_id).attr('id', `${patient_id.attr('id')}_${patient.user_id}`);
        $(patient_id).html(`${patient.user_id}`);

        let patient_dob = $(patient_wrapper).find('#patient_dob');
        $(patient_dob).attr('id', `${patient_dob.attr('id')}_${patient.user_id}`)
        $(patient_dob).html(moment(patient.user_dob, 'DD/MM/YYYY').format('ddd, Do MMM YY'))

        let patient_email = $(patient_wrapper).find('#patient_email');
        $(patient_email).attr('id', `${patient_email.attr('id')}_${patient.user_id}`);
        $(patient_email).html(`${patient.user_email}`);

        let appointments = $(patient_wrapper).find("#patient_appointment_count");
        $(appointments).attr('id', `${appointments.attr('id')}_${patient.user_id}`)
        $(appointments).html(upcoming_appointments_count(patient));

        return patient_wrapper
    } catch (err) {
        context_manager.post_exception('CLIENT_EXCEPTION_SCRIPT_PATIENT', err);
        context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
    }
}
