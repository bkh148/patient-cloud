/*
	Definition of an abstract component used across the dasboards.
	Components will share mandatory functionality to ensure updates work as expected with the pub / sub pattern.
*/

/* Definition */
let Component = function () {
  if (this.constructor == Component) {
    throw new Error('Can\'t instantiate abstract class.')
  }
};

/* Subscriptions are all objects this component will use in the context dictionary */
Component.prototype.subscriptions = []
Component.prototype.name = "abstract"

/* Show will show this component in the content div */
Component.prototype.show = function () {
  throw new Error('Cannot call an abstract method.')
}

/* Hide will remove this component from the content div */
Component.prototype.hide = function () {
  throw new Error('Cannot call an abstract method.')
}

/* Update will update the data in the component when in the content div */
Component.prototype.update = function () {
  throw new Error('Cannot call an abstract method.')
}


/*
	Component Factory
*/

let ComponentFactory = function () {
}

ComponentFactory.prototype.create_component = function (type) {
  switch (type) {
    case 'dashboard':
      return new DashboardComponent(type);
    case 'appointments':
      return new AppointmentComponent(type);
    case 'settings':
      return new SettingsComponent(type);
    case 'clinicians':
      return new ClinicianComponent(type);
    case 'care_locations':
      return new CareLocationsComponent(type);
    case 'patients':
      return new PatientsComponent(type);
    case 'data_analytics':
      return new DataAnalyticsComponent(type);
    default:
      throw new Error('Couldn\'t load component type.')
  }
};

/*
  Component Utilities
*/

function removeFadeOut(element, speed) {
  $(element).fadeOut(speed,
    function () {
      $(element).remove();
    });
}

function addFadeIn(element, parent, speed) {
  $(element).hide().appendTo(parent).fadeIn(speed);
}

/*
  Patient Component
*/

let PatientsComponent = function (name) {
  Component.apply(this, arguments)
  PatientsComponent.prototype.name = name;
}

PatientsComponent.prototype = Object.create(Component.prototype);
PatientsComponent.prototype.constructor = PatientsComponent;

PatientsComponent.prototype.subscriptions = ['patients']
PatientsComponent.prototype.name = "not_set"

PatientsComponent.prototype.show = function () {
  try {
    let patients_container = document.createElement('div');
    patients_container.setAttribute('id', `${PatientsComponent.prototype.name}-component`)

    let patient_markup = context_manager._cache.templates['users_container'];
    patients_container.innerHTML = patient_markup;

    let current_patients_container = $(patients_container).find('#current_user_container');
    let previous_patients_container = $(patients_container).find('#past_user_container');

    for (let i = 0; i < context_manager._cache.patients.length; i++) {
      let patient = context_manager._cache.patients[i];
      let patient_element = build_patient(patient);

      $(current_patients_container).append(patient_element);
    }

    addFadeIn(patients_container, '#content', 600);

  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_PATIENT', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

PatientsComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${PatientsComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_PATIENT', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

PatientsComponent.prototype.update = function () {
  console.log('Update the patients component.')
}


/*
	Dashboard component - used for some top level information details
*/
let DashboardComponent = function (name) {
  Component.apply(this, arguments)
  DashboardComponent.prototype.name = name
}

DashboardComponent.prototype = Object.create(Component.prototype);
DashboardComponent.prototype.constructor = DashboardComponent;

DashboardComponent.prototype.subscriptions = ['dashboard']
DashboardComponent.prototype.name = "not_set"

DashboardComponent.prototype.show = function () {
  console.log('Show the dashboard component.')
};

DashboardComponent.prototype.hide = function () {
  console.log('Hide the dashboard component.')
}

DashboardComponent.prototype.update = function () {
  console.log('Update the dashboard component.')
}

/*
    Appointment Component
*/

let AppointmentComponent = function (name) {
  Component.apply(this, arguments);
  AppointmentComponent.prototype.name = name
}

AppointmentComponent.prototype = Object.create(Component.prototype);
AppointmentComponent.prototype.constructor = AppointmentComponent;

AppointmentComponent.prototype.subscriptions = ['appointments']
AppointmentComponent.prototype.name = "not_set"

AppointmentComponent.prototype.show = function () {
  try {
    let appointments_container = document.createElement('div');
    appointments_container.setAttribute('id', `${AppointmentComponent.prototype.name}-component`)

    let appointment_container_markdown = context_manager._cache.templates['appointments_container'];
    appointments_container.innerHTML = appointment_container_markdown;

    let upcoming_appointments = $(appointments_container).find('#upcoming_appointments_container')
    let past_appointments = $(appointments_container).find('#past_appointments_container')

    for (let i = 0; i < context_manager._cache.appointments.length; i++) {
      let appointment = context_manager._cache.appointments[i];
      let appointment_element = build_appointment(appointment);

      if (moment() > moment(appointment['appointment_date_utc'])) {
        $(past_appointments).append(appointment_element)
      } else {
        $(upcoming_appointments).append(appointment_element)
      }
    }

    addFadeIn(appointments_container, '#content', 600);

  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_APPOINTMENT', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

AppointmentComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${AppointmentComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_APPOINTMENT', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

AppointmentComponent.prototype.update = function () {
  console.log('Update the appointments component.')
}

/*
  Clinician Component
*/

let ClinicianComponent = function (name) {
  Component.apply(this, arguments);
  ClinicianComponent.prototype.name = name
};

ClinicianComponent.prototype = Object.create(Component.prototype);
ClinicianComponent.prototype.constructor = ClinicianComponent;

ClinicianComponent.prototype.subscriptions = ['clinicians']
ClinicianComponent.prototype.name = "not_set"

ClinicianComponent.prototype.show = function () {
  try {
    let clinician_component = document.createElement('div');
    clinician_component.setAttribute('id', `${ClinicianComponent.prototype.name}-component`)

    let clinician_markdown = context_manager._cache.templates[ClinicianComponent.prototype.name];
    clinician_component.innerHTML = clinician_markdown;

    addFadeIn(clinician_component, '#content', 600);

  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_CLINICIAN', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

ClinicianComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${ClinicianComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_CLINICIAN', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

ClinicianComponent.prototype.update = function () {
  console.log('Update the care location components')
}

/*
   Care location Component
*/

let CareLocationsComponent = function (name) {
  Component.apply(this, arguments);
  CareLocationsComponent.prototype.name = name
};

CareLocationsComponent.prototype = Object.create(Component.prototype);
CareLocationsComponent.prototype.constructor = CareLocationsComponent;

CareLocationsComponent.prototype.subscriptions = ['care_locations']
CareLocationsComponent.prototype.name = "not_set"


CareLocationsComponent.prototype.show = function () {
  try {
    let care_location_component = document.createElement('div');
    care_location_component.setAttribute('id', `${CareLocationsComponent.prototype.name}-component`)

    let care_location_markup = context_manager._cache.templates[CareLocationsComponent.prototype.name];
    care_location_component.innerHTML = care_location_markup;

    addFadeIn(care_location_component, '#content', 600);

  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_CARELOCATION', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

CareLocationsComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${CareLocationsComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_CARELOCATION', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

CareLocationsComponent.prototype.update = function () {
  console.log('Update the care location components')
}

/* 
    Analytics Componenet
*/

let DataAnalyticsComponent = function (name) {
  Component.apply(this, arguments);
  DataAnalyticsComponent.prototype.name = name
};

DataAnalyticsComponent.prototype = Object.create(Component.prototype);
DataAnalyticsComponent.prototype.constructor = DataAnalyticsComponent;

DataAnalyticsComponent.prototype.subscriptions = ['data_analytics']
DataAnalyticsComponent.prototype.name = "not_set"

DataAnalyticsComponent.prototype.show = function () {
  try {
    let data_analytics_component = document.createElement('div');
    data_analytics_component.setAttribute('id', `${DataAnalyticsComponent.prototype.name}-component`)

    let data_analytics_markup = context_manager._cache.templates[DataAnalyticsComponent.prototype.name];
    data_analytics_component.innerHTML = data_analytics_markup;

    addFadeIn(data_analytics_component, '#content', 600);

  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_ANALYTICS', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

DataAnalyticsComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${DataAnalyticsComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_ANALYTICS', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}


DataAnalyticsComponent.prototype.update = function () {
  console.log('Update the data analytics components')
}


/*
Setting component - used for managing the user's settings
*/
let SettingsComponent = function (name) {
  Component.apply(this, arguments);
  SettingsComponent.prototype.name = name
};

SettingsComponent.prototype = Object.create(Component.prototype);
SettingsComponent.prototype.constructor = SettingsComponent;

SettingsComponent.prototype.subscriptions = ['settings']

SettingsComponent.prototype.show = function () {
  try {
    let settings_component = document.createElement('div');
    settings_component.setAttribute('id', `${SettingsComponent.prototype.name}-component`)

    let settings_markdown = context_manager._cache.templates[SettingsComponent.prototype.name];
    settings_component.innerHTML = settings_markdown;

    addFadeIn(settings_component, '#content', 600);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_SETTINGS', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

SettingsComponent.prototype.hide = function () {
  try {
    removeFadeOut(`#${SettingsComponent.prototype.name}-component`, 200);
  } catch (err) {
    context_manager.post_exception('CLIENT_EXCEPTION_COMPONENT_SETTINGS', err);
    context_manager.error_message(`An unexpected error has occurred, please try refreshing the page.`);
  }
}

SettingsComponent.prototype.update = function () {
  console.log('Update the settings component.')
}
