function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function validateName(name) {
    var re = /^[a-zA-Z]+(([',.-][a-zA-Z])?[a-zA-Z]*)*$/;
    return re.test(String(name).toLowerCase());
}


let validate_form = function(form, firstname_input, lastname_input, email_input, confirm_email_input) {

    let is_valid = true;

    // Validate first name
    let firstname_validator = $(form).find('#firstname-validator')
    $(firstname_validator).attr('class', '')

    if (validateName(firstname_input.val())) {
        $(firstname_validator).html('Looks good!')
        $(firstname_validator).addClass('valid-feedback')
    } else {
        $(firstname_validator).html('Invalid name.')
        $(firstname_validator).addClass('invalid-feedback d-block');
        is_valid = false;
    }

    // Validate last name
    let lastname_validator = $(form).find('#lastname-validator')
    $(lastname_validator).attr('class', '')

    if (validateName(lastname_input.val())) {
        $(lastname_validator).html('Looks good!')
        $(lastname_validator).addClass('valid-feedback')
    } else {
        $(lastname_validator).html('Invalid name');
        $(lastname_validator).addClass('invalid-feedback d-block');
        is_valid = false;
    }

    // Validate e-mail
    let email_validator = $(form).find('#email-validator')
    $(email_validator).attr('class', '')


    if (validateEmail($(email_input).val())) {
        $(email_validator).html('Looks good!')
        $(email_validator).addClass('valid-feedback')
    } else {
        $(email_validator).html('Please enter a valid e-mail.');
        $(email_validator).addClass('invalid-feedback d-block');
        is_valid = false;
    }

    // Validate confirmation
    let confirm_validator = $(form).find('#confirm-email-validator')
    $(confirm_validator).attr('class', '')

    if ($(email_input).val() == $(confirm_email_input).val()) {
        $(confirm_validator).html('E-mail addresses match!')
        $(confirm_validator).addClass('valid-feedback')
    } else {
        $(confirm_validator).html('E-mail addresses don\'t match.');
        $(confirm_validator).addClass('invalid-feedback d-block');
        is_valid = false;
    }

    // The form has been checked.
    form.classList.add('was-validated');

    return is_valid;
}

let close_form = function() {
    let form = document.getElementById('invite-form');
    $('#invite-user-model').modal("hide");
    $(form).attr('class', '');
    $(form).trigger('reset');
}
let submit_invite = function (form) {
    try {
        let form = document.getElementById('invite-form');
        let firstname_input = $(form).find('#invite-first-name');
        let lastname_input = $(form).find('#invite-last-name');
        let email_input = $(form).find('#invite-email');
        let confirm_email_input = $(form).find('#invite-confirm-email');

        if (validate_form(form, firstname_input, lastname_input, email_input, confirm_email_input)) {

            // Post request + close and clean the form on success
            let invite = {
                'invite_id': context_manager.new_guid(),
                'invited_by': context_manager._cache.settings.user['user_id'],
                'user_role_id': context_manager._cache.user_roles['PATIENT'],
                'invited_email': email_input.val(),
                'invited_first_name': firstname_input.val(),
                'invited_last_name': lastname_input.val(),
                'invited_on_utc': moment().utc().format(),
                'expiration_date_utc': moment().add(4, 'hours').utc().format()
            }
            
            close_form();
            
            $.ajax({
                url: `http://${context_manager._cache.configurations['host']}:${context_manager._cache.configurations['port']}/api/v1.0/invites/`,
                type: 'POST',
                beforeSend: function(request) {
                    request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
                },
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(invite),
                success: function() {
                    console.log("SUCCESS ON THE INVITE")
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    throw new Error(errorThrown)
                }
            })
        }

    } catch (err) {
        // Log exception
        console.log(`An error has occurred whilst posting the invite to the server: ${err}`)
    }
}
