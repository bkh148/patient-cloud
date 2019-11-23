from ..interfaces import ILocationService

class LocationService(ILocationService):

    def __init__(self, loc_repo, log_service):
        self._location_repo = loc_repo
        self._log_service = log_service

    def upsert_location(self, location):
        """update or insert a new location"""
        try:
            self._location_repo.upsert_location(location)
        except Exception as e:
            self._log_service.log_exception(e)

    def delete_location(self, location_id):
        """ remove a location from the datastor """ 
        try:
            self._location_repo.delete_location(location_id)
        except Exception as e:
            self._log_service.log_exception(e)

    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
        try:
            return self._location_repo.get_location_by_id(location_id)
        except Exception as e:
            self._log_service.log_exception(e)
        
        return None
    
    def get_locations_by_ids(self, id_list):
        """ return an array of locations """
        try:
            return self._location_repo.get_locations_by_ids(id_list)
        except Exception as e:
            self._log_service.log_exception(e)
            
        return []
    
    def get_all_locations(self):
        """ returns all care location """
        try:
            return self._location_repo.get_all_locations();
        except Exception as e:
            self._log_service.log_exception(e)
        
        return []
