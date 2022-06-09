from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Connection, Cursor

from shelvingManager.Models.item_type import ItemType

from shelvingManager.Backend.Controller.database_controller import DatabaseController

class ItemTypeController:

    cur_trace = None
    conn  = None

    def __init__(self, conn: Connection):
        self.conn = conn
        self.conn.set_trace_callback(print)
        self.cur_trace = self.conn.cursor()

    def insert_item_type(self, item_type: ItemType) -> bool:
        value = db.insert_item_type(item_type, self.cur_trace, self.conn)
        return value

    def get_item_type(self, item_type_id: int) -> ItemType:
        value = ItemType(db.get_item_type_object(item_type_id, self.cur_trace).fetchone())
        return value

    def get_all_item_types(self) -> list:
        item_types = []
        for row in db.get_all_item_types_object(self.cur_trace):
            item_types.append(row)
        value = item_types
        return value

    def delete_item_type(self, item_type_id: int, ) -> bool:
        value = db.delete_item_type(item_type_id, self.cur_trace, self.conn)
        return value

    def update_item_type(self, item_type: ItemType, ) -> bool:
        value = db.update_item_type(item_type, self.cur_trace, self.conn)
        return value

    def get_item_type_id(self, item_type_name: str, ) -> int:
        value = db.get_item_type_id(item_type_name, self.cur_trace)
        return value