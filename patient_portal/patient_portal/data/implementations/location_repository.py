from ..interfaces import ILocationRepository
import json

class LocationRepository(ILocationRepository):

    def __init__(self, db):
        self._db = db

    def upsert_location(self, location):
        """update or insert a new location"""

    def has_location(self, location_id):
        """ evaluate if a location is in the datastore """

    def delete_location(self, location_id):
        """ remove a location from the datastor """

    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
        return self._db.get_single("SELECT * FROM location WHERE location_id=?", (location_id, ))
    
    def get_all_locations(self):
        """ return all care locations currently in SQLite"""
        return self._db.get_all("SELECT * FROM location;")
