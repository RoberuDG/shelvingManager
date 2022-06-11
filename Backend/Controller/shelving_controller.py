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

    def insert_shelving(self, room_id: int, code: str, start: list, end: list, description= None) -> bool:
        position = {
            "start": start,
            "end": end
        }
        json = js.dumps(position)
        shelving = Shelving(room_id, code, json, description)
        value = db.insert_shelving(shelving, self.cur_trace, self.conn)
        return value

    def get_shelving_position(self, shelving_id: int) -> list:
        shelving = self.get_shelving(shelving_id)
        value = js.loads(shelving.position)
        position = [value["start"], value["end"]]
        return position

    def get_shelving(self, shelving_id: int) -> Shelving:
        value = db.get_shelving_object(shelving_id, self.cur_trace).fetchone()
        shelving = Shelving(value[1], value[2], value[3], value[4], value[0])
        return shelving

    def get_all_shelvings(self) -> list:
        shelvings = []
        for row in db.get_all_shelvings_object(self.cur_trace):
            if row is not None:
                shelving = Shelving(row[1], row[2], row[3], row[4], row[0])
                shelvings.append(shelving)
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
                shelving = Shelving(row[1], row[2], row[3], row[4], row[0])
                shelvings.append(shelving)
        value = shelvings
        return value