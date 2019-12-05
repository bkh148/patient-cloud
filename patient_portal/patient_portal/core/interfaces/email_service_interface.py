import abc


class IEmailService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_user_invite(self, invite):
        """ Send a user invitation """
