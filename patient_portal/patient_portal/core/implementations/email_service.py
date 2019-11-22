from ..interfaces import IEmailService
from flask_mail import Message
from flask import render_template

class EmailService(IEmailService):
    
    def __init__(self, mail_server, invite_repo, log_service):
        self._mail_server = mail_server
        self._invite_repo = invite_repo
        self._log_service = log_service
        
    def send_user_invite(self, subject, recipients, recipient_name, body, action_title, action_url):
        """ send a user invite to a given address 
    
        Args:
            subject: e-mail subject,
            recipients: one or more e-mail addresses to send the e-mail to,
            body: message to be injected into the Jinja2 templates,
            action_title: title to appear on the e-mail link button,
            action_url: url to redirect user to when clicking on button
        """
        try:
            msg = Message('Invitation to Patient Portal', sender='liamlambwebtech@gmail.com', recipients=recipients)
            msg.html = render_template('email_template.html', email={
                'recipient': recipient_name,
                'body': body,
                'image_source': 'https://gallery.mailchimp.com/9014f17a146c8e9c77c04d5c0/images/e06fc039-13f0-45d5-b451-2c886a2af106.png',
                'action_title': action_title,
                'action_url': action_url
            })
            self._mail_server.send(msg)
            
            # Log activity: email
        except Exception as e:
            self._log_service.log_exception(e)
            raise
