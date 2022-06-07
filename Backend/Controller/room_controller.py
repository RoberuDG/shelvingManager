from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.room import Room


class RoomController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_room(room: Room, cur: Cursor) -> bool:
        return db.insert_room(room, cur)

    def get_room(room_id: int, cur: Cursor) -> Room:
        return Room(db.get_room_object(room_id, cur).fetchone())

    def get_all_rooms(cur: Cursor) -> list:
        rooms = []
        for row in db.get_all_rooms_object(cur):
            if row is not None:
                room = Room(row[0], row[1], row[3], row[2])
                rooms.append(room)
        return rooms

    def delete_room(room_id: int, cur: Cursor) -> bool:
        return db.delete_room(room_id, cur)

    def update_room(room: Room, cur: Cursor) -> bool:
        return db.update_room(room, cur)

    def get_room_id(room_name: str, cur: Cursor) -> int:
        return db.get_room_id(room_name, cur)