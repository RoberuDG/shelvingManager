import sqlite3
from sqlite3 import Connection, Cursor
import os
from xmlrpc.client import Boolean

from shelvingManager.Models.room import Habitacion

class DatabaseUtils:

    def __connect_to_db__() -> Connection:
        con = sqlite3.connect('/home/gragak/Code/shelvingManager/shelvingManager/Backend/database/prueba.db')

    def create_db(connection: Connection) -> Boolean:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../scripts/sql.sqlite')

        with open(filename, 'r') as file:
            data = file.read()

        return True if connection.executescript(data).lastrowid > 0 else False

    #TODO:Implementar métodos de inserción, borrado y modificación de filas

    ### *Lectura de datos
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

    ### *Inserción de datos
    def insert_room(room: Habitacion, cur: Cursor) -> Boolean:
        cur.execute('''INSERT INTO rooms VALUES ({room.name}, {room.description}, {room.positions}, {room.creation_date})''', room.name, room.description, room.positions, room.creation_date)

        return True if cur.lastrowid > 0 else False