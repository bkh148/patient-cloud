import abc


class ILocationService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def upsert_location(self, location):
        """update or insert a new location"""

    @abc.abstractmethod
    def delete_location(self, location_id):
        """ remove a location from the datastor """

    @abc.abstractmethod
    def get_user_location(self, user_id):
        """ return a location of a user """

    @abc.abstractmethod
    def get_locations_by_ids(self, id_list):
        """ return an array of locations """

    @abc.abstractmethod
    def get_location_by_id(self, location_id):
        """ return a given location object by its id """

    @abc.abstractmethod
    def get_all_locations(self):
        """ returns all care location """
