from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection

from shelvingManager.Models.item import Item


class ItemController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_item(self, item: Item) -> bool:
        value = db.insert_item(item, self.cur_trace, self.conn)
        return value

    def get_item(self, item_id: int) -> Item:
        item = Item(db.get_item_object(item_id, self.cur_trace).fetchone())
        return item

    def get_all_items(self) -> list:
        items = []
        for row in db.get_all_items_object(self.cur_trace):
            items.append(row)
        return items

    def delete_item(self, item_id: int) -> bool:
        value = db.delete_item(item_id, self.cur_trace, self.conn)
        return value

    def update_item(self, item: Item) -> bool:
        value = db.update_item(item, self.cur_trace, self.conn)
        return value

    def get_item_id(self, item_name: str) -> int:
        value = db.get_item_id(item_name, self.cur_trace)
        return value

    def get_items_by_shelf_id(self, shelve_id: int) -> list:
        items = []
        for row in db.get_items_by_shelf_id(shelve_id, self.cur_trace):
            if row is not None:
                item = Item(row[0], row[1], row[2], row[3], row[4], row[5])
                items.append(item)
        return items