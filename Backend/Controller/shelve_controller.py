from Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.shelve import Shelve


class ShelveController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_shelve(shelve: Shelve, cur: Cursor) -> bool:
        return db.insert_shelve(shelve, cur)

    def get_shelve(shelve_id: int, cur: Cursor) -> Shelve:
        return Shelve(db.get_shelve_object(shelve_id, cur).fetchone())

    def get_all_shelves(shelve: Shelve, cur: Cursor) -> Shelve[any]:
        shelves = []
        for row in db.get_all_shelves_object(shelve, cur):
            shelves.append(row)
        return shelves

    def delete_shelve(shelve_id: int, cur: Cursor) -> bool:
        return db.delete_shelve(shelve_id, cur)

    def update_shelve(shelve: Shelve, cur: Cursor) -> bool:
        return db.update_shelve(shelve, cur)
