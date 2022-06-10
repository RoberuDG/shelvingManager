from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection

from shelvingManager.Models.shelving import Shelving

import json as js

class ShelvingController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_shelving(self, shelving: Shelving) -> bool:
        value = db.insert_shelving(shelving, self.cur_trace, self.conn)
        return value

    def get_shelving(self, shelving_id: int) -> Shelving:
        value = Shelving(db.get_shelving_object(shelving_id, self.cur_trace).fetchone())
        return value

    def get_all_shelvings(self) -> list:
        shelvings = []
        for row in db.get_all_shelvings_object(self.cur_trace):
            shelvings.append(row)
        value = shelvings
        return value

    def delete_shelving(self, shelving_id: int) -> bool:
        value = db.delete_shelving(shelving_id, self.cur_trace, self.conn)
        return value

    def update_shelving(self, shelving: Shelving) -> bool:
        value = db.update_shelving(shelving, self.cur_trace, self.conn)
        return value

    def get_shelving_id(self, shelving_name: str) -> int:
        value = db.get_shelving_id(shelving_name, self.cur_trace)
        return value

    def get_shelvings_by_room_id(self, room_id: int) -> list:
        shelvings = []
        for row in db.get_shelving_by_room_id(room_id, self.cur_trace):
            if row is not None:
                shelving = Shelving(row[0], row[1], row[2], row[3])
                shelvings.append(shelving)
        value = shelvings
        return value