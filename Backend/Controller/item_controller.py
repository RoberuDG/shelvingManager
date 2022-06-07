from shelvingManager.Backend.Database.database import DatabaseUtils as db

from sqlite3 import Cursor

from shelvingManager.Models.item import Item

class ItemController:

    def __init__(self, cur: Cursor):
        self.cur = cur

    def insert_item(item: Item, cur: Cursor) -> bool:
        return db.insert_item(item, cur)

    def get_item(item_id: int, cur: Cursor) -> Item:
        return Item(db.get_item_object(item_id, cur).fetchone())

    def get_all_items(cur: Cursor):
        items = []
        for row in db.get_all_items_object(cur):
            items.append(row)
        return items

    def delete_item(item_id: int, cur: Cursor) -> bool:
        return db.delete_item(item_id, cur)

    def update_item(item: Item, cur: Cursor) -> bool:
        return db.update_item(item, cur)

    def get_item_id(item_name: str, cur: Cursor) -> int:
        return db.get_item_id(item_name, cur)