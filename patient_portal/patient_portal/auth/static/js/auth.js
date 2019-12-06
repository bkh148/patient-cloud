$(function () {
  $('#user-dob').datetimepicker({
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
  } else {
    $(forename_validator).html('Invalid name!');
    $(forename_input).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let surname_validator = $(form).find('#surname-validator');

  if (surname_input.val().match(name_pattern) != null) {
    $(surname_validator).html('Looks good!');
    $(surname_validator).attr('class', 'valid-feedback');
  } else {
    $(surname_validator).html('Invalid name!');
    $(surname_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let date_validator = $(form).find('#date-validator');

  if (dob_input.val().match(date_pattern) != null) {
    $(date_validator).html('Looks good!');
    $(date_validator).attr('class', 'valid-feedback');
  } else {
    $(date_validator).html('Please select a valid date!');
    $(date_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let password_validator = $(form).find('#password-validator');

  if (password_input.val().match(password_input) != null) {
    $(password_validator).html('Password looks good!');
    $(password_validator).attr('class', 'valid-feedback');
  } else {
    $(password_validator).html('Your password must contain a special character and digit. Password length must be minimum 8 characters.');
    $(password_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  }

  let confirm_validator = $(form).find('#confirm-validator');

  if (password_input.val() != confirm_input.val()) {
    $(confirm_validator).html('Passwords must match!');
    $(confirm_validator).attr('class', 'invalid-feedback d-block');
    is_valid = false;
  } else {
    $(confirm_validator).html('Passwords match!');
    $(confirm_validator).attr('class', 'valid-feedback');
  }

  $(form).addClass('was-validated')

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

