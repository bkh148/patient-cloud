/*
	Definition of an abstract component used across the dasboards.
	Components will share mandatory functionality to ensure updates work as expected with the pub / sub pattern.
*/

/* Definition */
let Component = function() {
  if (this.constructor == Component) {
    throw new Error('Can\'t instantiate abstract class.')
  }
};

/* Subscriptions are all objects this component will use in the context dictionary */
Component.prototype.subscriptions = []
Component.prototype.name = "abstract"

/* Show will show this component in the content div */
Component.prototype.show = function() {
    throw new Error('Cannot call an abstract method.')
}

/* Hide will remove this component from the content div */
Component.prototype.hide = function() {
    throw new Error('Cannot call an abstract method.')
}

/* Update will update the data in the component when in the content div */
Component.prototype.update = function() {
    throw new Error('Cannot call an abstract method.')
}


/*
	Component Factory
*/

let ComponentFactory = function() {
}

ComponentFactory.prototype.create_component = function(type) {
    switch(type) {
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
  Patient Component
*/

let PatientsComponent = function(name) {
  Component.apply(this, arguments)
  PatientsComponent.prototype.name = name;
}

PatientsComponent.prototype = Object.create(Component.prototype);
PatientsComponent.prototype.constructor = PatientsComponent;

PatientsComponent.prototype.subscriptions = ['patients']
PatientsComponent.prototype.name = "not_set"

PatientsComponent.prototype.show = function() {
  console.log('Show the patients component.')
};

PatientsComponent.prototype.hide = function() {
  console.log('Hide the patients component.')
}

PatientsComponent.prototype.update = function() {
  console.log('Update the patients component.')
}


/*
	Dashboard component - used for some top level information details
*/
let DashboardComponent = function(name) {
  Component.apply(this, arguments)
  DashboardComponent.prototype.name = name
}

DashboardComponent.prototype = Object.create(Component.prototype);
DashboardComponent.prototype.constructor = DashboardComponent;

DashboardComponent.prototype.subscriptions = ['dashboard']
DashboardComponent.prototype.name = "not_set"

DashboardComponent.prototype.show = function() {
  console.log('Show the dashboard component.')
};

DashboardComponent.prototype.hide = function() {
  console.log('Hide the dashboard component.')
}

DashboardComponent.prototype.update = function() {
  console.log('Update the dashboard component.')
}

/*
    Appointment Component
*/

let AppointmentComponent = function(name) {
  Component.apply(this, arguments);
  AppointmentComponent.prototype.name = name
}

AppointmentComponent.prototype = Object.create(Component.prototype);
AppointmentComponent.prototype.constructor = AppointmentComponent;

AppointmentComponent.prototype.subscriptions = ['appointments']
AppointmentComponent.prototype.name = "not_set"

AppointmentComponent.prototype.show = function() {
  $('#appointments-component').removeClass('d-none');
}

AppointmentComponent.prototype.hide = function() {
  $('#appointments-component').addClass('d-none');
}

AppointmentComponent.prototype.update = function() {
  console.log('Update the appointments component.')
}

/*
  Clinician Component
*/

let ClinicianComponent = function(name) {
  Component.apply(this, arguments);
  ClinicianComponent.prototype.name = name
};

ClinicianComponent.prototype = Object.create(Component.prototype);
ClinicianComponent.prototype.constructor = ClinicianComponent;

ClinicianComponent.prototype.subscriptions = ['clinicians']
ClinicianComponent.prototype.name = "not_set"

ClinicianComponent.prototype.show = function() {
  console.log('Show the care location component.')
}

ClinicianComponent.prototype.hide = function() {
  console.log('Hide the care location components')
}

ClinicianComponent.prototype.update = function() {
  console.log('Update the care location components')
}

/*
   Care location Component
*/

let CareLocationsComponent = function(name) {
  Component.apply(this, arguments);
  CareLocationsComponent.prototype.name = name
};

CareLocationsComponent.prototype = Object.create(Component.prototype);
CareLocationsComponent.prototype.constructor = CareLocationsComponent;

CareLocationsComponent.prototype.subscriptions = ['care_locations']
CareLocationsComponent.prototype.name = "not_set"

CareLocationsComponent.prototype.show = function() {
  console.log('Show the care location component.')
}

CareLocationsComponent.prototype.hide = function() {
  console.log('Hide the care location components')
}

CareLocationsComponent.prototype.update = function() {
  console.log('Update the care location components')
}

/* 
    Analytics Componenet
*/

let DataAnalyticsComponent = function(name) {
  Component.apply(this, arguments);
  DataAnalyticsComponent.prototype.name = name
};

DataAnalyticsComponent.prototype = Object.create(Component.prototype);
DataAnalyticsComponent.prototype.constructor = DataAnalyticsComponent;

DataAnalyticsComponent.prototype.subscriptions = ['data_analytics']
DataAnalyticsComponent.prototype.name = "not_set"

DataAnalyticsComponent.prototype.show = function() {
  console.log('Show the data analytics component.')
}

DataAnalyticsComponent.prototype.hide = function() {
  console.log('Hide the data analytics components')
}

DataAnalyticsComponent.prototype.update = function() {
  console.log('Update the data analytics components')
}


/*
Setting component - used for managing the user's settings
*/
let SettingsComponent = function(name) {
  Component.apply(this, arguments);
  SettingsComponent.prototype.name = name
};

SettingsComponent.prototype = Object.create(Component.prototype);
SettingsComponent.prototype.constructor = SettingsComponent;

SettingsComponent.prototype.subscriptions = ['settings']

SettingsComponent.prototype.show = function() {
  console.log('Show the settings component')
}

SettingsComponent.prototype.hide = function() {
  console.log('Hide the settings component')
}

SettingsComponent.prototype.update = function() {
  console.log('Update the settings component')
}


