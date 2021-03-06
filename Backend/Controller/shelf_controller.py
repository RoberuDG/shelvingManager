from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection

from shelvingManager.Models.shelf import Shelf

import json as js


class ShelfController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_shelf(self, shelf: Shelf) -> bool:
        return db.insert_shelve(shelf, self.cur_trace, self.conn)

    def get_shelf(self, shelf_id: int) -> Shelf:
        value = Shelf(db.get_shelve_object(shelf_id, self.cur_trace).fetchone())
        return value

    def get_all_shelves(self) -> list:
        shelves = []
        for row in db.get_all_shelves_object(self.cur_trace):
            if row is not None:
                shelf = Shelf(row[0], row[1], row[2], row[3])
                shelves.append(shelf)
        value = shelves
        return value

    def delete_shelf(self, shelf_id: int) -> bool:
        value = db.delete_shelve(shelf_id, self.cur_trace, self.conn)
        return value

    def update_shelf(self, shelf: Shelf) -> bool:
        value = db.update_shelf(shelf, shelf.id, self.cur_trace, self.conn)
        return value

    def get_shelf_id(self, shelf_name: str) -> int:
        value = db.get_shelve_id(shelf_name, self.cur_trace)
        return value

    def get_shelves_by_shelving_id(self, shelving_id: int) -> list:
        shelves = []
        for row in db.get_shelves_by_shelving_id(shelving_id, self.cur_trace):
            if row is not None:
                shelf = Shelf(row[1], row[2], row[3], row[0])
                shelves.append(shelf)
        value = shelves
        return value

    def get_shelf_by_shelving_id_and_shelf_pos(self, shelving_id: int, shelf_pos: int) -> Shelf:
        value = db.get_shelf_by_shelving_id_and_shelf_pos(shelving_id, shelf_pos, self.cur_trace).fetchone()
        shelf = Shelf(value[1], value[2], value[3], value[0])
        return shelf
