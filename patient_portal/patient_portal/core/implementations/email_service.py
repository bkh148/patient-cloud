from ..interfaces import IEmailService
from flask_mail import Message
from flask import render_template

class EmailService(IEmailService):

    def __init__(self, mail_server, invite_repo, user_service, log_service):
        self._mail_server = mail_server
        self._invite_repo = invite_repo
        self._user_service = user_service
        self._log_service = log_service

    # TODO: These should all be moved out into strategy pattern to encourage growth.

    def __send_admin_invite(self, invite_id, recipient_email, recipient_first_name, recipient_last_name, sender_firstname):
        try:
            subject = "Admin Invitation"
            action_url = "https://google.co.uk/{}".format(invite_id)
            action_title = "Join as Admin"
            message = """
            {} has invited you to join the Patient Portal platform as an administrator.
            This will grant you access to manage all care locations within our system, as
            well being able to have an overview of the system's metrics. Please click on the link
            below to accept your invitation. You will then be redirect to an authentication page 
            where you can set you password for the platform. 
            
            Please note that this invitation will expire in a few hours.
            
            We are very pleased to have you on board,
            The Patient Portal Team""".format(sender_firstname)

            self.__send_message(
                subject, "{} {}".format(recipient_first_name, recipient_last_name), [recipient_email], message, action_title, action_url)
            # Log activity: email
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def __send_local_admin_invite(self, invite_id, recipient_email, recipient_first_name, recipient_last_name, sender_firstname):
        try:
            subject = "Local Admin Invitation"
            action_url = "https://google.co.uk/{}".format(invite_id)
            action_title = "Join as Local Admin"
            message = """
            {} has invited you to join the Patient Portal platform as an local administrator.
            This will grant you access to manage all clinicians within your care location.
            Please click on the link below to accept your invitation. 
            You will then be redirect to an authentication page where you can set you password for the platform. 
            
            Please note that this invitation will expire in a few hours.
            
            We are very pleased to have you on board,
            The Patient Portal Team""".format(sender_firstname)

            self.__send_message(
                subject, "{} {}".format(recipient_first_name, recipient_last_name), [recipient_email], message, action_title, action_url)
            # Log activity: email
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def __send_clinician_invite(self, invite_id, recipient_email, recipient_first_name, recipient_last_name, sender_firstname):
        try:
            subject = "Clinician Invitation"
            action_url = "https://google.co.uk/{}".format(invite_id)
            action_title = "Join as Clinician"
            message = """
            {} has invited you to join the Patient Portal as a clinician in your care location.
            This will grant you access to manage all of your patients within this care location.
            Please click on the link below to accept your invitation. 
            You will then be redirect to an authentication page where you can set you password for the platform. 
            
            Please note that this invitation will expire in a few hours.
            
            We are very pleased to have you on board,
            The Patient Portal Team""".format(sender_firstname)

            self.__send_message(
                subject, "{} {}".format(recipient_first_name, recipient_last_name), [recipient_email], message, action_title, action_url)

            # Log activity: email
        except Exception as e:
            self._log_service.log_exception(e)
            raise

    def __send_patient_invite(self, invite_id, recipient_email, recipient_first_name, recipient_last_name, sender_lastname):
        try:
            subject = "Patient Invitation"
            action_url = "https://google.co.uk/{}".format(invite_id)
            action_title = "Join as Patient"
            message = """
            Dr. {} has invited you to join Patient Portal as a new patient.
            This will allow you to manage all of your medical details throughout your care.
            Please click on the link below to accept your invitation. 
            You will then be redirect to an authentication page where you can set you password for the platform. 
            
            Please note that this invitation will expire in a few hours.
            
            We are very pleased to have you on board,
            The Patient Portal Team""".format(sender_lastname)

            self.__send_message(
                subject, "{} {}".format(recipient_first_name, recipient_last_name), [recipient_email], message, action_title, action_url)
            # Log activity: email
        except Exception as e:
            self._log_service.log_exception(e)
            raise


    def __send_message(self, subject, recipient_name, recipients, body, action_title, action_url):
        msg = Message(subject, sender='liamlambwebtech@gmail.com',
                      recipients=recipients)
        msg.html = render_template('email_template.html', email={
            'recipient': recipient_name,
            'body': body,
            'image_source': 'https://gallery.mailchimp.com/9014f17a146c8e9c77c04d5c0/images/e06fc039-13f0-45d5-b451-2c886a2af106.png',
            'action_title': action_title,
            'action_url': action_url
        })
        self._mail_server.send(msg)
        

    def send_user_invite(self, invite):
        
        invite_id = invite['invite_id']
        recipient_firstname = invite['invited_first_name']
        recipient_lastname = invite['invited_last_name']
        recipient_email = invite['invited_email']
        user_role = invite['user_role_id']
        sender_id = invite['invited_by']
        
        sender = self._user_service.get_user_by_id(sender_id)
        user_role = self._user_service.get_user_role(user_role);
        
        print("SENDER: {}".format(sender))
        print("ROLE: {}".format(user_role))
        
        if user_role['user_role'] == "ADMIN":
            self.__send_admin_invite(invite_id, recipient_email, recipient_firstname, recipient_lastname, sender['user_forname'])
        elif user_role['user_role'] == "LOCAL_ADMIN":
            self.__send_local_admin_invite(invite_id, recipient_email, recipient_firstname, recipient_lastname, sender['user_forname'])
        elif user_role['user_role'] == "CLINICIAN":
            self.__send_clinician_invite(invite_id, recipient_email, recipient_firstname, recipient_lastname, sender['user_forname'])
        else:
            self.__send_patient_invite(invite_id, recipient_email, recipient_firstname, recipient_lastname, sender['user_lastname'])
            
