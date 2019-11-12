## Thoughts for report
---


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
