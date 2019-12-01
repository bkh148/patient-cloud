//TODO FIX THIS WHOLE FILE :(

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validateName(name) {
    var re = /^[a-zA-Z]+(([',.-][a-zA-Z])?[a-zA-Z]*)*$/;
    return re.test(String(name).toLowerCase());
}


let validate_form = function(form, forename_input, surname_input, email_input, confirm_email_input) {

    let is_valid = true;

    // Validate first name
    let firstname_validator = $(form).find('#forename-validator')

    if (validateName(forename_input.val())) {
        $(firstname_validator).html('Looks good!')
        $(firstname_validator).attr('class', 'valid-feedback')
    } else {
        $(firstname_validator).html('Invalid name.')
        $(firstname_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    // Validate last name
    let lastname_validator = $(form).find('#surname-validator')

    if (validateName(surname_input.val())) {
        $(lastname_validator).html('Looks good!')
        $(lastname_validator).attr('class', 'valid-feedback')
    } else {
        $(lastname_validator).html('Invalid name');
        $(lastname_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    // Validate e-mail
    let email_validator = $(form).find('#email-validator')

    if (validateEmail($(email_input).val())) {
        $(email_validator).html('Looks good!')
        $(email_validator).attr('class', 'valid-feedback')
    } else {
        $(email_validator).html('Please enter a valid e-mail.');
        $(email_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    // Validate confirmation
    let confirm_validator = $(form).find('#confirm-email-validator')

    if ($(email_input).val() == $(confirm_email_input).val()) {
        $(confirm_validator).html('E-mail addresses match!')
        $(confirm_validator).attr('class', 'valid-feedback')
    } else {
        $(confirm_validator).html('E-mail addresses don\'t match.');
        $(confirm_validator).attr('class', 'invalid-feedback d-block');
        is_valid = false;
    }

    // The form has been checked.
    $(form).addClass('was-validated');

    return is_valid;
}

let close_form = function() {
    let form = document.getElementById('invite-form');

    deactivate_loading(form);
    $('#invite-user-model').modal("hide");
    $(form).attr('class', '');
    $(form).trigger('reset');
}

let activate_loading = function(form) {
    let cancel_submit = $(form).find('#submit-cancel-form');
    let submit = $(form).find('#submit-invite-form');

    let spinner_markdown = `<span id="invite-sending-spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Sending...`;
    $(submit).html(spinner_markdown);

    $(cancel_submit).prop('disabled', true);
    $(submit).prop('disabled', true);
}

let deactivate_loading = function(form) {
    let cancel_submit = $(form).find('#submit-cancel-form');
    let submit = $(form).find('#submit-invite-form');

    $(submit).html("Send Invite");

    $(cancel_submit).prop('disabled', false);
    $(submit).prop('disabled', false);
}

let submit_invite = function(form) {
    try {

        //let form = document.getElementById('invite-form');
        let forename_input = $(form).find('#invite-forename');
        let surname_input = $(form).find('#invite-surname');
        let email_input = $(form).find('#invite-email');
        let confirm_email_input = $(form).find('#invite-confirm-email');

        if (validate_form(form, forename_input, surname_input, email_input, confirm_email_input)) {
            
            activate_loading(form);

            let invite = {
                'invite_id': context_manager.new_guid(),
                'invited_by': context_manager._cache.settings.user.user_id,
                'user_role_id': context_manager._cache.user_roles['PATIENT'],
                'invited_email': email_input.val(),
                'invited_forename': forename_input.val(),
                'invited_surname': surname_input.val(),
                'assign_to_location': context_manager._cache.settings.care_location.location_id,
                'invited_on_utc': moment().utc().format(),
                'expiration_date_utc': moment().add(4, 'hours').utc().format()
            }
            
            $.ajax({
                url: `http://${context_manager._cache.configurations['host']}:${context_manager._cache.configurations['port']}/api/v1.0/invites/`,
                type: 'POST',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
                },
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(invite),
                success: function() {
                    context_manager.success_message('Success!', `Your invitation has successfully been sent to ${invite['invited_forename']} ${invite['invited_surname']} at: ${invite['invited_email']}!`);
                    close_form();
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    context_manager.post_exception('post_exception', errorThrown);
                    context_manager.error_message('Oops!', `Your invitation for ${invite['invited_forename']} ${invite['invited_surname']} failed to send. Please try again.`);

                    deactivate_loading(form);
                }
            })
        }

    } catch (err) {
        context_manager.post_exception('post_exception', err);
        context_manager.error_message('Oops!', `An unexpected error has occurred whilst sending your invitation, please try again.`);

        deactivate_loading(form);
    }
}
