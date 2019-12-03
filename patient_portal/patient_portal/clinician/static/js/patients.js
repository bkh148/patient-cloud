let format_name = function (name) {
    return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
}

let create_appointment = function (patient) {
    return function () {
        console.log(patient);
    }
}

let edit_patient = function (patient_id) {
    return function () {
        context_manager.info_message("The ability to edit patients data will be added in a feature version of Patient Portal.", true);
    }
}

let transfer_patient = function (patient_id) {
    return function () {
        context_manager.info_message("The ability to transfer patients will be added in a feature version of Patient Portal.", true);
    }
}

let update_status_badge = function(user_id, status) {
    let status_badge = $(`#status-badge_${user_id}`);
    $(status_badge).attr('class', `badge-status badge-${status}`);
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
        $(patient_name).html(`${format_name(patient.user_surname)}, ${format_name(patient.user_forename)}`);

        // Status badge
        let patient_badge = $(patient_wrapper).find('#status-badge');
        $(patient_badge).attr('id', `${patient_badge.attr('id')}_${patient.user_id}`);

        if (context_manager._cache.online_users[`${patient.user_id}`] !== undefined) {
            $(patient_badge).addClass('badge-online');
        } else {
            $(patient_badge).addClass('badge-offline');
        }

        // New appointment button
        let new_appointment_button = $(patient_wrapper).find('#new_appointment');
        $(new_appointment_button).attr('id', `${new_appointment_button.attr('id')}_${patient.user_id}`);
        $(new_appointment_button).on('click', create_appointment(patient));

        // Edit user button
        let edit_patient_button = $(patient_wrapper).find('#edit_patient');
        $(edit_patient_button).attr('id', `${edit_patient_button.attr('id')}_${patient.user_id}`);
        $(edit_patient_button).on('click', edit_patient(patient));

        // Transfer of care button
        let transfer_of_care = $(patient_wrapper).find('#transfer_patient');
        $(transfer_of_care).attr('id', `${transfer_of_care.attr('id')}_${patient.user_id}`);
        $(transfer_of_care).on('click', transfer_patient(patient));


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

        return patient_wrapper
    } catch (err) {
        console.log(`An error has occurred whilst building a patient element: ${err}`);
        context_manager.post_exception('CLIENT_EXCEPTION_PATIENTS', err);
    }
}