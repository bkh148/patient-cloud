from ..interfaces import ILocationService

class LocationService(ILocationService):

    def __init__(self, repo):
        self._repo = repo

    def upsert_location(self, location):
        """update or insert a new location"""
        self._repo.upsert_location(location)

    def delete_location(self, location_id):
        """ remove a location from the datastor """
        self._repo.delete_location(location_id)

    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
        return self._repo.get_location_by_id(location_id)
