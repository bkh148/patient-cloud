import abc

class ILocationRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def upsert_location(self, location):
        """update or insert a new location"""

    @abc.abstractmethod
    def has_location(self, location_id):
        """ evaluate if a location is in the datastore """

    @abc.abstractmethod
    def delete_location(self, location_id):
        """ remove a location from the datastor """

    @abc.abstractmethod
    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
