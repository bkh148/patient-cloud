let handle_incoming_appointment = function (appointment) {
    try {
        if (context_manager._cache.appointments.length == 0) {
            context_manager._cache.appointments.push(appointment);
        } else {
            for (let i = 0; i < context_manager._cache.appointments.length; i++) {
                if (moment(appointment.appointment_date_utc).isBefore(moment(context_manager._cache.appointments[i].appointment_date_utc))) {
                    context_manager._cache.appointments.splice(i, 0, appointment);
                    break;
                }

                if (i == context_manager._cache.appointments.length - 1) {
                    context_manager._cache.appointments.push(appointment);
                    break;
                }
            }
        }

        if (context_manager.current_context == "appointments") {
            context_manager.update_component("appointments");
        } else {
            // TODO: Notification badege when not in context!
        }

        context_manager.info_message(`Your clinician Dr. ${context_manager._cache.settings.clinician.user_surname} has scheduled a new appointment for your on ${moment(appointment.appointment_date_utc).format('dddd Do MMM YYYY')}.`);
    } catch (err) {
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENT', err);
        context_manager.error_message(`An unexpected error has occurred whilst handling an incoming appointment, please reload the page.`);
    }
}

let handle_cancelled_appointment = function (appointment_id) {
    try {
        let date_copy;
        for(let i = 0; i < context_manager._cache.appointments.length; i++) {
            let cached_appointment = context_manager._cache.appointments[i];
    
            if (cached_appointment != undefined) {
                if (cached_appointment.appointment_id == appointment_id) {
                    date_copy = { 'appointment_date_utc': cached_appointment.appointment_date_utc };
                    context_manager._cache.appointments.splice(i, 1);
                    break;
                }
            }
        }

        if (context_manager.current_context == "appointments") {
            context_manager.update_component("appointments");
        }

        context_manager.info_message(`Your clinician Dr. ${context_manager._cache.settings.clinician.user_surname} has cancelled your scheduled appointment on ${moment(date_copy.appointment_date_utc).format('dddd Do MMM YYYY')}.`);

    } catch (err) {
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENT', err);
        context_manager.error_message(`An unexpected error has occurred whilst handling a deleted appointment, please reload the page.`);
    }
}

let build_appointment = function (appointment) {
    try {


        // TODO: Centralise 

        let appointment_wrapper = document.createElement('div')
        appointment_wrapper.setAttribute('id', `appointment_wrapper_${appointment.appointment_id}`)
        appointment_wrapper.innerHTML = context_manager._cache.templates.appointments_item;

        // Get and set the left date element
        let left_date = $(appointment_wrapper).find('#appointment-date-left');
        let left_date_value = moment(appointment.appointment_date_utc).format('dddd Do MMM YY');
        $(left_date).attr('id', `${left_date.attr('id')}_${appointment.appointment_id}`)
        $(left_date).html(left_date_value)

        // Get and set the right date element
        let right_date = $(appointment_wrapper).find('#appointment-date-right');
        let right_date_value = moment(appointment.appointment_date_utc).format('hh:mm a');
        $(right_date).attr('id', `${right_date.attr('id')}_${appointment.appointment_id}`);
        $(right_date).html(right_date_value)

        let location;
        for (let i = 0; i < context_manager._cache.locations.length; i++) {
            let temp = context_manager._cache.locations[i]

            if (temp.location_id == appointment.location_id) {
                location = temp;
                break;
            }
        }

        if (location == null || location == undefined) {
            throw new Error("Could not load location from context manager.");
        }

        let location_name = $(appointment_wrapper).find('#appointment-location-name');
        $(location_name).attr('id', `${location_name.attr('id')}_${appointment.appointment_id}`);
        $(location_name).html(location.location_name)

        let location_address = $(appointment_wrapper).find('#appointment-location-address');
        $(location_address).attr('id', `${location_address.attr('id')}_${appointment.appointment_id}`);
        $(location_address).html(`${location.location_address}, `)

        let location_postcode = $(appointment_wrapper).find('#appointment-location-postcode');
        $(location_postcode).attr('id', `${location_postcode.attr('id')}_${appointment.appointment_id}`);
        $(location_postcode).html(`${location.location_postcode}, `)

        let location_city = $(appointment_wrapper).find('#appointment-location-city');
        $(location_city).attr('id', `${location_city.attr('id')}_${appointment.appointment_id}`);
        $(location_city).html(`${location.location_city}, `)

        let appointment_reason = $(appointment_wrapper).find('#appointment-reason');
        $(appointment_reason).attr('id', `${appointment_reason.attr('id')}_${appointment.appointment_id}`);
        $(appointment_reason).html(appointment.appointment_type)

        let appointment_notes = $(appointment_wrapper).find('#appointment-notes');
        $(appointment_notes).attr('id', `${appointment_notes.attr('id')}_${appointment.appointment_id}`);
        $(appointment_notes).html(appointment.appointment_notes)


        return appointment_wrapper
    } catch (err) {
        console.log(`An error has occurred whilst building an appointment element. ${err}`)
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENTS', err)
    }
}

