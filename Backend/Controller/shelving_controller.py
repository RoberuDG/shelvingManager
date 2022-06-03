from Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.shelving import Shelving


class ShelvingController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_shelving(shelving: Shelving, cur: Cursor) -> bool:
        return db.insert_shelving(shelving, cur)

    def get_shelving(shelving_id: int, cur: Cursor) -> Shelving:
        return Shelving(db.get_shelving_object(shelving_id, cur).fetchone())

    def get_all_shelvings(shelving: Shelving, cur: Cursor) -> Shelving[any]:
        shelvings = []
        for row in db.get_all_shelvings_object(shelving, cur):
            shelvings.append(row)
        return shelvings

    def delete_shelving(shelving_id: int, cur: Cursor) -> bool:
        return db.delete_shelving(shelving_id, cur)

    def update_shelving(shelving: Shelving, cur: Cursor) -> bool:
        return db.update_shelving(shelving, cur)
