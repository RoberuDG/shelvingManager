from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.shelf import Shelf


class ShelfController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_shelf(shelf: Shelf, cur: Cursor) -> bool:
        return db.insert_shelve(shelf, cur)

    def get_shelf(shelf_id: int, cur: Cursor) -> Shelf:
        return Shelf(db.get_shelves_object(shelf_id, cur).fetchone())

    def get_all_shelves(cur: Cursor):
        shelfs = []
        for row in db.get_all_shelves_object(cur):
            if row is not None:
                shelf = Shelf(row[0], row[1], row[2], row[3])
                shelfs.append(shelf)
            shelfs.append(row)
        return shelfs

    def delete_shelf(shelf_id: int, cur: Cursor) -> bool:
        return db.delete_shelve(shelf_id, cur)

    def update_shelf(shelf: Shelf, cur: Cursor) -> bool:
        return db.update_shelve(shelf, cur)

    def get_shelf_id(shelf_name: str, cur: Cursor) -> int:
        return db.get_shelve_id(shelf_name, cur)

    def get_shelve_by_shelving_id(shelving_id: int, cur: Cursor) -> Shelf:
        shelves = []
        for row in db.get_shelves_by_shelving_id(shelving_id, cur):
            if row is not None:
                shelf = Shelf(row[0], row[1], row[2], row[3])
                shelves.append(shelf)
        return shelves
