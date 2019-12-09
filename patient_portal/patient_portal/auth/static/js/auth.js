$(function () {
  $('#user-dob-group').datetimepicker({
    format: 'DD/MM/YYYY',
    //dayViewHeaderFormat: 'dddd Do MMM YY'
  });
});

const name_pattern = /^[a-zA-Z]+(([',.-][a-zA-Z])?[a-zA-Z]*)*$/;
const password_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[(){}!#$_%&? "])(?=.*[A-Z]).{8,}$/;
const date_pattern = /^((?:0[0-9])|(?:[1-2][0-9])|(?:3[0-1]))\/((?:0[1-9])|(?:1[0-2]))\/((?:19|20)\d{2})$/;

let validate_login = function () {
  let is_valid = true;

  return is_valid;
}

let validate_create_login = function (form, forename_input, surname_input, dob_input, password_input, confirm_input) {
  let is_valid = true;

  let forename_validator = $(form).find('#forename-validator');

  if (forename_input.val().match(name_pattern) != null) {
    $(forename_validator).html('Looks good!');
    $(forename_validator).attr('class', 'valid-feedback');
    $(forename_input).attr('class', 'form-control is-valid');
  } else {
    $(forename_validator).html('Invalid name!');
    $(forename_input).attr('class', 'invalid-feedback d-block');
    $(forename_input).attr('class', 'form-control is-invalid');
    is_valid = false;
  }

  let surname_validator = $(form).find('#surname-validator');

  if (surname_input.val().match(name_pattern) != null) {
    $(surname_validator).html('Looks good!');
    $(surname_validator).attr('class', 'valid-feedback');
    $(surname_input).attr('class', 'form-control is-valid');
  } else {
    $(surname_validator).html('Invalid name!');
    $(surname_validator).attr('class', 'invalid-feedback d-block');
    $(surname_input).attr('class', 'form-control is-invalid');
    is_valid = false;
  }

  let date_validator = $(form).find('#date-validator');

  if (dob_input.val().match(date_pattern) != null) {
    $(date_validator).html('Looks good!');
    $(dob_input).attr('class', 'form-control datetimepicker-input is-valid');
    $(date_validator).attr('class', 'valid-feedback');
  } else {
    $(date_validator).html('Please select a valid date!');
    $(dob_input).attr('class', 'form-control datetimepicker-input is-invalid');
    $(date_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let password_validator = $(form).find('#password-validator');

  if (password_input.val().match(password_pattern) != null) {
    $(password_validator).html('Password looks good!');
    $(password_input).attr('class', 'form-control is-valid');
    $(password_validator).attr('class', 'valid-feedback');
  } else {
    $(password_validator).html('Your password must contain a special character and digit. Password length must be minimum 8 characters.');
    $(password_input).attr('class', 'form-control is-invalid');
    $(password_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let confirm_validator = $(form).find('#confirm-validator');

  if (confirm_input.val() == "") {
    $(confirm_validator).html('Password field cannot be empty!');
    $(confirm_input).attr('class', 'form-control is-invalid');
    $(confirm_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }
  else if (password_input.val() != confirm_input.val()) {
    $(confirm_validator).html('Passwords must match!');
    $(confirm_input).attr('class', 'form-control is-invalid');
    $(confirm_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  } else {
    $(confirm_validator).html('Passwords match!');
    $(confirm_input).attr('class', 'form-control is-valid');
    $(confirm_validator).attr('class', 'valid-feedback');
  }

  return is_valid;
}

$('#confirm-login-form').submit(function (event) {
  event.preventDefault();
  let forename = $(this).find('#user-forename');
  let surname = $(this).find('#user-surname');
  let dob = $(this).find('#user-dob');
  let password = $(this).find('#user-password');
  let confirm = $(this).find('#user-confirm-password');

  if (validate_create_login(this, forename, surname, dob, password, confirm)) {
    console.log("Submit")
    this.submit();
  }
});

