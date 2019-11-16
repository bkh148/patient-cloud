import abc

class IEmailService(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def send_user_invite(self, sender, invited, invite_type):
        """ send a user invite to a given address 
        
        Args:
            sender: user object sending the invite
            invited: model holding data of recipient (fname, lname, email)
            invite_type: type of role the new user will be granted (Admin, Local Admin, Clinician, Patient)
        """
