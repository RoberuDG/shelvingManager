from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection

from shelvingManager.Models.item import Item

import json as js

class ItemController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_item(self, name, shelf_id: int, item_type_id: int, start_position: int, end_position: int, description: int) -> bool:
        positions = {
            'start_position': start_position,
            'end_position': end_position
        }
        json = js.dumps(positions)
        item = Item(shelf_id, item_type_id, name, json, description)
        value = db.insert_item(item, self.cur_trace, self.conn)
        return value

    def get_item_position(self, item_id: int) -> list:
        item = self.get_item(item_id)
        value = js.loads(item.position)
        size = [value["start_position"], value["end_position"]]
        return size

    def get_item(self, item_id: int) -> Item:
        value = db.get_item_object(item_id, self.cur_trace).fetchone()
        item = Item(value[1], value[2], value[4], value[3], value[5], value[0])
        return item

    def get_all_items(self) -> list:
        items = []
        for row in db.get_all_items_object(self.cur_trace):
            if row is not None:
                item = Item(row[1], row[2], row[4], row[3], row[5], row[0])
                items.append(item)
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

    def get_items_by_shelf_id(self, shelf_id: int) -> list:
        items = []
        for row in db.get_items_by_shelf_id(shelf_id, self.cur_trace):
            if row is not None:
                item = Item(row[1], row[2], row[3], row[4], row[5], row[0])
                items.append(item)
        return items