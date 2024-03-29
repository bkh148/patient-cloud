## Thoughts for report
---

**Jinja Templates and Client side rendering :** <br />
A core feature in flask applications is to use Jinja template rendering. Jinja is fairly easy to use and in most you don't really need to do much more than what is suggested in the documentation. When developing the appointments page for patient, an unexpected issue was encountered, that is that I just didn't plan ahead as much as I should have. Initially, the server would render the appointments templates on page load. It would go through the services to pull out any appointments, and then render an appointments template which ready to go data. Once the page loaded, the context manager would simply take that template html and place it into the relevant container to be rendered on the DOM. 

The initial idea was ok, but I soon realized that I needed a way to have these templates available on the client, too. This is because when a clinician makes a new appointment, if the target patient is online, they will receive an instant notification about this appointment. The context manager therefore receives the appointment meta data, and would then render a new DOM element in the appropriate appointments container element. However, because the appointments were pre-rendered on the server, I would have to write a JavaScript template for new appointments and load them on page load in order to be able to build my new appointment object - which means duplication of code. To get around this, I decided that on the initial load of a user's dashboard, the server will send all of the necessary templates the client will need for any dynamic logic. This is done by using Jinja2, which will all required render templates with placeholder values. Once the client loads the dashboard, the context manager will get any required templates from the context managers cache (location: context_manager._cache.templates). This optimizes code re-use and prevent me from needing to write client side logic for building the appointments html element.

**Application Cron Jobs :**<br />
Some features that are currently sitting in the code base, don't actually need to be part of the project.
This is because they are features that do not depend on any aspect of the application. One could argue that some features could actually slow down the user's experience if network connections were to poor. <br />
The features in mind are the cleaning and maintenance of the invite service, and the e-mail service. <br />

The e-mail service currently sends out an e-mail to anyone who has been invited by some user to join the platform. This isn't really an issue in itself, but it may be wiser to abstract this out, as this would mean that if we were to spin up ```n``` instances of the application, then they will ```all``` be handling sending e-mails, which seems like a bad idea. <br />

A better architecture may be to have a deamon service running in the background with similar configurations than that of the running server instances. This service would setup a connection to the database, and poll the invite table every so minutes to check for new e-mails to send out the new users. <br />

The benefit of this kind of service, is we could add as many cron jobs as we want. Each job will be responsible for doing some form of periodic work. For instance, the issue with the invitation table at the moment, is we currently store a heap of already used invitiations. <br />
Although, one could argue it would be good to keep these invites for debugging purposes, it maybe be wise to periodically move consumed invitations to a archive database, and delete any invites that were't consumed, or were flagged as erroneous.

This would also be a be a good idea around the log table. Logs typically get very large, very quickly, and could easily start causing issues on larger application. It would therfore be wise, to periodically move logs out into a serperate database. It would be interesting to have a database dump per month or week for instance, which could be individually cleaned by some other service to be used for data analysis.

**Database design drawbacks :**<br />
Due to experience levels in designing an implementing databases, a few issues were encountered whilst putting this project together. Designing a role based database can be quite a complex task if one wants to make sure it can grow beyond the initial thoughts. This is exactly the issue in the current database design. <br />
During development I realized that I had no way of mapping patients to clinicians without having a mapping table explicitly for this purpose. This raise a number of concerns about the fundamentals of the platform:
    * What if a clinician is also a local admin ?
    * What if an admin is also a patient ?
And many more.. <br />
This demands a better design of how roles are managed in the projects, and raises thoughts around active directories and the use of groups and group inheritance for making sure that the platform's role management could grow in the future.

**Git Strategies :** <br />
It's quite easy when developing to have a few bad when using git. As 3rd year students, it's important that we start moving towards getting our hands a bit dirty with git and really trying to enforce good habits. One of the issues that this project had was a bad habit around branching strategies. Generally, I find it's good to keep master completely and utterly clean. This means, that only code that has been tested and reviewed should actually every be merge back into master. 

Furthermore, in terms of history of work, and feature management, it's generally a wise idea to add features by branch. This means that whenever a chunk of work has just been finished, tested and merged back into master, we will create a new branch off the latest master snapshot when we intend to develop a new feature. Commits would therefore be pushed to that branch, and this really allows a good overview of a particular features progress before it being pulled into the master branch. This allows for a final read of the work, and another opportunity to spot any bugs or inconsistencies.

**Swagger Documentation :** <br />
Discussion on the importance of swagger within teams but also on open APIS


**Service / Repository Abstractions :** <br />
Discussion on the use of the core, and data layers for abstractions.


**Observer pattern around the online users :** <br />


**Encryption of medical data :** <br />
Discuss how we decided not to look into data encryption for now, as I would like to do this across the application.
This could include discussions on Diffie Hellman, and the public keys exchange between two secret clients (clinician / patient)

**Server Setup :** <br />
```
export FLASK_ENV=...
export SECRET_KEY=...
export MAIL_SERVER=...
export MAIL_USERNAME=...
export MAIL_PASSWORD=...
```


**DEBUG MODE :** <br />
Because of a known issue in Flask Socket IO, in order to run the application in debug mode, you need to do the following: <br />
```
export FLASK_ENV=development
export FLASK_APP=patient_portal/start_up.py
```

and run the following command: ```python3 patient_portal/__main__.py``` <br />
REFERENCE: https://github.com/miguelgrinberg/Flask-SocketIO/issues/817
