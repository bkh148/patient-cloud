from ..interfaces import ILocationRepository
import json


class LocationRepository(ILocationRepository):

    def __init__(self, db):
        self._db = db

    def upsert_location(self, location):
        """update or insert a new location"""
        if self.has_location(location['location_id']):
            self._db.update('location', location)
        else:
            self._db.insert('location', location)

    def has_location(self, location_id):
        """ evaluate if a location is in the datastore """
        return self._db.count("""
            SELECT COUNT() FROM location
            WHERE location_id = ?""", (location_id, )) > 0

    def delete_location(self, location_id):
        """ remove a location from the datastor """
        self._db.execute("""
            DELETE FROM location
            WHERE location_id = ?""", (location_id, ))

    def get_user_location(self, user_id):
        """ return a location of a user """
        return self._db.get_single("""
        SELECT location_id, location_name, location_coord_x, location_coord_y, location_postcode, location_address, location_city
        FROM user t1
        LEFT JOIN user_role_map t2 ON t1.user_role_map_id = t2.user_role_map_id
        LEFT JOIN location t3 ON t2.location_id = t3.location_id
        WHERE user_id = ?""", (user_id, ))

    def get_locations_by_ids(self, id_list):
        """ return an array of locations """

        query = """
        SELECT * FROM location
            WHERE location_id IN ({})""".format(','.join('?' * len(id_list)))

        return self._db.get_all(query, id_list)

    def get_location_by_id(self, location_id):
        """ return a given location object by its id """
        return self._db.get_single("SELECT * FROM location WHERE location_id=?", (location_id, ))

    def get_all_locations(self):
        """ return all care locations currently in SQLite"""
        return self._db.get_all("SELECT * FROM location")
