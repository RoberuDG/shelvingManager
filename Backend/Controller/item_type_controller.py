from Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.item_type import ItemType


class ItemTypeController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_item_type(item_type: ItemType, cur: Cursor) -> bool:
        return db.insert_item_type(item_type, cur)

    def get_item_type(item_type_id: int, cur: Cursor) -> ItemType:
        return ItemType(db.get_item_type_object(item_type_id, cur).fetchone())

    def get_all_item_types(item_type: ItemType, cur: Cursor) -> ItemType[any]:
        item_types = []
        for row in db.get_all_item_types_object(item_type, cur):
            item_types.append(row)
        return item_types

    def delete_item_type(item_type_id: int, cur: Cursor) -> bool:
        return db.delete_item_type(item_type_id, cur)

    def update_item_type(item_type: ItemType, cur: Cursor) -> bool:
        return db.update_item_type(item_type, cur)
