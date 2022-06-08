from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.shelving import Shelving


class ShelvingController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_shelving(shelving: Shelving, cur: Cursor) -> bool:
        return db.insert_shelving(shelving, cur)

    def get_shelving(shelving_id: int, cur: Cursor) -> Shelving:
        return Shelving(db.get_shelving_object(shelving_id, cur).fetchone())

    def get_all_shelvings(cur: Cursor) -> list:
        shelvings = []
        for row in db.get_all_shelvings_object(cur):
            shelvings.append(row)
        return shelvings

    def delete_shelving(shelving_id: int, cur: Cursor) -> bool:
        return db.delete_shelving(shelving_id, cur)

    def update_shelving(shelving: Shelving, cur: Cursor) -> bool:
        return db.update_shelving(shelving, cur)

    def get_shelving_id(shelving_name: str, cur: Cursor) -> int:
        return db.get_shelving_id(shelving_name, cur)

    def get_shelvings_by_room_id(room_id: int, cur: Cursor) -> list:
        shelvings = []
        for row in db.get_shelving_by_room_id(room_id, cur):
            if row is not None:
                shelving = Shelving(row[0], row[1], row[2], row[3])
                shelvings.append(shelving)
        return shelvings