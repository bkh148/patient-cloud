from ..interfaces import ILocationService

class LocationService(ILocationService):

    def __init__(self, loc_repo):
        self._location_repo = loc_repo

    def upsert_location(self, location):
        """update or insert a new location"""
        self._location_repo.upsert_location(location)

    def delete_location(self, location_id):
        """ remove a location from the datastor """
        self._location_repo.delete_location(location_id)

    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
        return self._location_repo.get_location_by_id(location_id)
    
    def get_all_locations(self):
        """ returns all care location """
        try:
            
            # log activity
            return self._location_repo.get_all_locations();
            
        except Exception as e:
            # log exception
            print("Service Exception | {} : {}".format(__name__, e))
        
        return []
