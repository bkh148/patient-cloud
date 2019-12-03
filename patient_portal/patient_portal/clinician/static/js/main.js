let user_logged_out = function(data) {
    // If current context is patient, update the patient component

    if (context_manager.current_context == "patients") {
        update_status_badge(data['user_id'], 'offline');
    }
}

let user_logged_in = function(data) {
    // If current context is patient, update the patient component
    if (context_manager.current_context == "patients") {
        update_status_badge(data['user_id'], 'online');
    }
}

let handle_data_received = function(data) {

}
