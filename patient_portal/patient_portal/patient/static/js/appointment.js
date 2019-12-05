let handle_incoming_appointment = function(appointment) {

    if (context_manager._cache.appointments.length == 0) {
        context_manager._cache.appointments.push(appointment);
    } else {
        for(let i = 0; i < context_manager._cache.appointments.length; i++) {
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
        let component = undefined;
        

        for (let i = 0; i < context_manager.components.length; i++) {
            component = context_manager.components[i];

            if (component.name == "appointments") {
                component.hide();
                component.show();
                break;
            }
        }

        context_manager.info_message(`Your clinician Dr. ${context_manager._cache.settings.clinician.user_surname} has scheduled a new appointment for your on ${moment(appointment.appointment_date_utc).format('dddd Do MMM YYYY')}.`);

    } else {

        // Notification Badge
        // If the badge is already existant
        // 
    }
}

let build_appointment = function(appointment) {
    try {
        let appointment_wrapper = document.createElement('div')
        appointment_wrapper.setAttribute('id', `appointment_wrapper_${appointment.appointment_id}`)
        appointment_wrapper.innerHTML = context_manager._cache.templates.appointments_item;

        // Get and set the left date element
        let left_date = $(appointment_wrapper).find('#appointment_date_left');
        let left_date_value = moment(appointment.appointment_date_utc).format('dddd Do MMM YY');
        $(left_date).attr('id', `${left_date.attr('id')}_${appointment.appointment_id}`)
        $(left_date).html(left_date_value)

        // Get and set the right date element
        let right_date = $(appointment_wrapper).find('#appointment_date_right');
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

        let location_name = $(appointment_wrapper).find('#appointment_location_name');
        $(location_name).attr('id', `${location_name.attr('id')}_${appointment.appointment_id}`);
        $(location_name).html(location.location_name)

        let location_address = $(appointment_wrapper).find('#appointment_location_address');
        $(location_address).attr('id', `${location_address.attr('id')}_${appointment.appointment_id}`);
        $(location_address).html(`${location.location_address}, `)

        let location_postcode = $(appointment_wrapper).find('#appointment_location_postcode');
        $(location_postcode).attr('id', `${location_postcode.attr('id')}_${appointment.appointment_id}`);
        $(location_postcode).html(`${location.location_postcode}, `)

        let location_city = $(appointment_wrapper).find('#appointment_location_city');
        $(location_city).attr('id', `${location_city.attr('id')}_${appointment.appointment_id}`);
        $(location_city).html(`${location.location_city}, `)

        let appointment_reason = $(appointment_wrapper).find('#appointment_reason');
        $(appointment_reason).attr('id', `${appointment_reason.attr('id')}_${appointment.appointment_id}`);
        $(appointment_reason).html(appointment.appointment_type)

        let appointment_notes = $(appointment_wrapper).find('#appointment_notes');
        $(appointment_notes).attr('id', `${appointment_notes.attr('id')}_${appointment.appointment_id}`);
        $(appointment_notes).html(appointment.appointment_notes)


        return appointment_wrapper
    } catch (err) {
        console.log(`An error has occurred whilst building an appointment element. ${err}`)
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENTS', err)
    }
}

