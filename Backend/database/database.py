import sqlite3
from sqlite3 import Connection, Cursor
import os
from xmlrpc.client import Boolean
from shelvingManager.Models.item import Item
from shelvingManager.Models.item_types import ItemType

from shelvingManager.Models.room import Habitacion
from shelvingManager.Models.shelve import Shelve
from shelvingManager.Models.shelving import Shelving


class DatabaseUtils:

    def __connect_to_db__() -> Connection:
        con = sqlite3.connect(
            '/home/gragak/Code/shelvingManager/shelvingManager/Backend/database/prueba.db')

    def create_db(connection: Connection) -> Boolean:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../scripts/sql.sqlite')

        with open(filename, 'r') as file:
            data = file.read()

        return True if connection.executescript(data).lastrowid > 0 else False

    # TODO:Implementar métodos de inserción, borrado y modificación de filas

    # *Lectura de datos
    def get_room(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM rooms WHERE room_id = {room_id}''', room_id)

    def get_shelve(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelves WHERE shelve_id = {shelve_id}''', shelve_id)

    def get_item_type(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM item_types WHERE item_type_type_id = {item_type_type_id}''', item_type_id)

    def get_item(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM items WHERE item_id = {item_id}''', item_id)

    def get_all_rooms(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM rooms ORDER BY id''')

    def get_all_shelvings(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelvings ORDER BY id''')

    def get_all_shelves(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelves ORDER BY id''')

    def get_all_item_types(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelving_types ORDER BY id''')

    def get_all_items(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM items ORDER BY id''')

    # *Inserción de datos
    def insert_room(room: Habitacion, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO rooms VALUES ({room.name}, {room.description}, {room.positions}, {room.creation_date})''',
                    room.name, room.description, room.positions, room.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_shelving(shelving: Shelving, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO shelvings VALUES ({shelving.room_id}, {shelving.code}, {shelving.positions}, {shelving.creation_date})''',
                    shelving.room_id, shelving.code, shelving.positions, shelving.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_shelve(shelve: Shelve, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO shelves VALUES ({shelve.shelving_id}, {shelve.code}, {shelve.order}, {shelve.creation_date})''',
                    shelve.shelving_id, shelve.code, shelve.order, shelve.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_item_type(item_type: ItemType, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO item_type VALUES ({item_type.name}, {item_type.description}, {item_type.positions})''',
                    item_type.name, item_type.description, item_type.positions)
        return True if cur.lastrowid > 0 else False

    def insert_item(item: Item, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO item VALUES ({item.shelving_id}, {item.item_type_id}, {item.position}, {item.code}, {item.name}, {item.description}, {item.is_active}''',
                    item.shelving_id, item.item_type_id, item.position, item.code, item.name, item.description, True)
        return True if cur.lastrowid > 0 else False

    # *Actualización de datos

    def update_room(room_id: int, room: Habitacion, cur: Cursor) -> Boolean:
        cur.execute('''UPDATE rooms SET name= {room.name}, description= {room.description}, positions= {room.positions} WHERE room_id= {room_id}''',
                    room.name, room.description, room.positions, room_id)
        return True if cur.lastrowid > 0 else False

    def update_shelving(shelving: Shelving, shelving_id: int, cur: Cursor) -> Boolean:
        cur.execute('''UPDATE shelving SET room_id= {shelving.room_id}, code= {shelving.code}, positions= {shelving.positions} WHERE shelving_id= {shelving_id}''',
                    shelving.room_id, shelving.code, shelving.positions, shelving_id)
        return True if cur.lastrowid > 0 else False

    def update_shelve(shelve: Shelve, shelve_id: int, cur: Cursor) -> Boolean:
        cur.execute('''UPDATE shelve SET shelve_id= {shelve.shelve_id}, code= {shelve.code}, order= {shelve.order} WHERE shelve_id= {shelve_id}''',
                    shelve.shelving_id, shelve.code, shelve.order, shelve_id)
        return True if cur.lastrowid > 0 else False

    def update_item_type(item_type: ItemType, item_type_id: int, cur: Cursor) -> Boolean:
        cur.execute('''UPDATE item_type SET name= {item_type.name}, description= {item_type.description}, positions= {item_type.positions} WHERE item_type_id= {item_type_id}''',
                    item_type.name, item_type.description, item_type.positions, item_type_id)
        return True if cur.lastrowid > 0 else False

    def update_item(item: Item, item_id: int, cur: Cursor) -> Boolean:
        cur.execute('''UPDATE item SET shelve_id= {item.shelve_id}, item_type_id= {item.item_type_id} , position= {item.position} ,name= {item.name}, description= {item.description}, is_active= {item.is_active} WHERE id= {item_id}''',
                    item.shelve_id, item.item_type_id, item.position, item.name, item.description, True, item_id)
        return True if cur.lastrowid > 0 else False

    # *Desactivacion de datos
    def deactivate_room(room_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''UPDATE room SET is_active = FALSE WHERE id= {room_id}''', room_id)
        return True if cur.lastrowid > 0 else False

    def deactivate_shelving(shelving_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''UPDATE shelving SET is_active = FALSE WHERE id= {shelving_id}''', shelving_id)
        return True if cur.lastrowid > 0 else False

    def deactivate_shelve(shelve_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''UPDATE shelve SET is_active = FALSE WHERE id= {shelve_id}''', shelve_id)
        return True if cur.lastrowid > 0 else False

    def deactivate_item_type(item_type_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''UPDATE item_type SET is_active = FALSE WHERE id= {item_type_id}''', item_type_id)
        return True if cur.lastrowid > 0 else False

    def deactivate_item(item_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''UPDATE item SET is_active = FALSE WHERE id= {item_id}''', item_id)
        return True if cur.lastrowid > 0 else False

    # *Borrado de datos
    def delete_room(room_id: int, cur: Cursor) -> Boolean:
        cur.execute('''DELETE FROM room WHERE id= {room_id}''', room_id)
        return True if cur.lastrowid > 0 else False

    def delete_shelving(shelving_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''DELETE FROM shelving WHERE id = {shelving_id}''', shelving_id)
        return True if cur.lastrowid > 0 else False

    def delete_shelve(shelve_id: int, cur: Cursor) -> Boolean:
        cur.execute(
            '''DELETE FROM shelve WHERE id = {shelve_id}''', shelve_id)
        return True if cur.lastrowid > 0 else False

    def delete_item(item_id: int, cur: Cursor) -> Boolean:
        cur.execute('''DELETE FROM item WHERE id = {item_id}''', item_id)
        return True if cur.lastrowid > 0 else False

    def delete_item_type(item_type_id: int, cur: Cursor) -> Boolean:
        cur.execute('''DELETE FROM item_type WHERE id = {item_type_id}''', item_type_id)
        return True if cur.lastrowid > 0 else False
