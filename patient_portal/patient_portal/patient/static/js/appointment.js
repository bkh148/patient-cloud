let build_appointment = function(appointment_json) {
    try {
        let appointment_wrapper = document.createElement('div')
        appointment_wrapper.setAttribute('id', `appointment_wrapper_${appointment_json['appointment_id']}`)
        appointment_wrapper.innerHTML = context_manager._cache.templates['appointments_item'];

        // Get and set the left date element
        let left_date = $(appointment_wrapper).find('#appointment_date_left');
        let left_date_value = moment(appointment_json['appointment_date_utc']).format('dddd Do MMM YY');
        $(left_date).attr('id', `${left_date.attr('id')}_${appointment_json['appointment_id']}`)
        $(left_date).html(left_date_value)

        // Get and set the right date element
        let right_date = $(appointment_wrapper).find('#appointment_date_right');
        let right_date_value = moment(appointment_json['appointment_date_utc']).format('hh:mm a');
        $(right_date).attr('id', `${right_date.attr('id')}_${appointment_json['appointment_id']}`);
        $(right_date).html(right_date_value)



        let location;
        for (let i = 0; i < context_manager._cache.locations.length; i++) {
            let temp = context_manager._cache.locations[i]

            if (temp['location_id'] == appointment_json['location_id']) {
                location = temp;
                break;
            }
        }

        if (location == null || location == undefined) {
            throw new Error("Could not load location from context manager.");
        }

        let location_name = $(appointment_wrapper).find('#appointment_location_name');
        $(location_name).attr('id', `${location_name.attr('id')}_${appointment_json['appointment_id']}`);
        $(location_name).html(location['location_name'])

        let location_address = $(appointment_wrapper).find('#appointment_location_address');
        $(location_address).attr('id', `${location_address.attr('id')}_${appointment_json['appointment_id']}`);
        $(location_address).html(`${location['location_address']}, `)

        let location_postcode = $(appointment_wrapper).find('#appointment_location_postcode');
        $(location_postcode).attr('id', `${location_postcode.attr('id')}_${appointment_json['appointment_id']}`);
        $(location_postcode).html(`${location['location_postcode']}, `)

        let location_city = $(appointment_wrapper).find('#appointment_location_city');
        $(location_city).attr('id', `${location_city.attr('id')}_${appointment_json['appointment_id']}`);
        $(location_city).html(`${location['location_city']}, `)

        let appointment_reason = $(appointment_wrapper).find('#appointment_reason');
        $(appointment_reason).attr('id', `${appointment_reason.attr('id')}_${appointment_json['appointment_id']}`);
        $(appointment_reason).html(appointment_json['appointment_type'])

        let appointment_notes = $(appointment_wrapper).find('#appointment_notes');
        $(appointment_notes).attr('id', `${appointment_notes.attr('id')}_${appointment_json['appointment_id']}`);
        $(appointment_notes).html(appointment_json['appointment_notes'])


        return appointment_wrapper
    } catch (err) {
        console.log(`An error has occurred whilst building an appointment element. ${err}`)
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENTS', err)
    }
}

