let build_appointment = function(appointment_json) {
    try {
        console.log("Build clinician appointment...")
    } catch (err) {
        console.log(`An error has occurred whilst building an appointment element. ${err}`)
        context_manager.post_exception('CLIENT_EXCEPTION_APPOINTMENTS', err)
    }
}

