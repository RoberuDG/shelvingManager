from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection

from shelvingManager.Models.room import Room

import json as js


class RoomController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_room(self, name: str, size_x: int, size_y: int, description=None) -> bool:
        positions = {
            "size_x": size_x,
            "size_y": size_y
        }
        json = js.dumps(positions)
        room = Room(name, json, description)
        value = db.insert_room(room, self.cur_trace, self.conn)
        return value

    def get_room(self, room_id: int) -> Room:
        value = db.get_room_object(room_id, self.cur_trace).fetchone()
        room = Room(value[1], value[3], value[2], value[0])
        return room

    def get_room_size(self, room_id: int) -> list:
        room = self.get_room(room_id)
        value = js.loads(room.positions)
        size = [value["size_x"], value["size_y"]]
        return size

    def get_all_rooms(self) -> list:
        rooms = []
        for row in db.get_all_rooms_object(self.cur_trace):
            if row is not None:
                room = Room(row[1], row[2], row[3], row[0])
                rooms.append(room)
        value = rooms
        return value

    def delete_room(self, room_id: int) -> bool:
        value = db.delete_room(room_id, self.cur_trace, self.conn)
        return value

    def update_room(self, room: Room) -> bool:
        value = db.update_room(room, self.cur_trace, self.conn)
        return value

    def get_room_id(self, room_name: str) -> int:
        value = db.get_room_id(room_name, self.cur_trace)
        return value
