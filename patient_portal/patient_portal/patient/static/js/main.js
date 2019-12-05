let user_logged_out = function(data) {

}

let user_logged_in = function(data) {

}

let handle_data_received = function(data) {

    let temp = data['appointment'];
    // if payload contains appointment, then a clinician is notifying of an appointment.
    if (data['appointment'] != undefined) {
        handle_incoming_appointment(data['appointment']);
    }

    if (data['appointment-cancelled'] != undefined) {
        handle_cancelled_appointment(data['appointment-cancelled']);
    }
}
