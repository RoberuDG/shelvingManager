from calendar import c
import sqlite3
from sqlite3 import Connection, Cursor, Error
import os
from shelvingManager.Models.item import Item
from shelvingManager.Models.item_type import ItemType

from shelvingManager.Models.room import Room, Room
from shelvingManager.Models.shelve import Shelve
from shelvingManager.Models.shelving import Shelving


class DatabaseUtils:

    def connect_to_db() -> Connection:
        try:
            print("Conectando a la base de datos")
            con = sqlite3.connect(
                'prueba.db')
            print("Conexión exitosa")
        except Error as e:
            print("Error al conectar a la base de datos")
        return con

    def create_db(connection: Connection) -> bool:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'script.sql')

        with open(filename, 'r') as file:
            data = file.read()

        try:
            connection.executescript(data)
            print ("Base de datos creada")
            return True
        except Error as e:
            print("Error al crear la base de datos")
            return False

    # *Lectura de datos

        # *Métodos de lectura total
    def get_room(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM rooms WHERE room_id = {room_id} ''', room_id)

    def get_shelving(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelvings WHERE id = {shelving_id} ''', shelving_id)

    def get_shelve(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelves WHERE shelve_id = {shelve_id} ''', shelve_id)

    def get_item_type(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM item_types WHERE item_type_type_id = {item_type_type_id} ''', item_type_id)

    def get_item(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM items WHERE item_id = {item_id} ''', item_id)

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

        # *Métodos de lectura de objetos
    def get_room_object(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, name, description, positions FROM rooms WHERE room_id = {room_id} ''', room_id)

    def get_shelving_object(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id, code, positions FROM shelves WHERE shelving_id = {shelving_id} ''', shelving_id)

    def get_shelve_object(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves WHERE shelve_id = {shelve_id} ''', shelve_id)

    def get_item_type_object(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types WHERE item_type_type_id = {item_type_type_id} ''', item_type_id)

    def get_item_object(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items WHERE item_id = {item_id} ''', item_id)

    def get_room_object(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM rooms WHERE room_id = {room_id} ''', room_id)

    def get_shelving_object(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id, code, positions FROM shelves WHERE shelving_id = {shelving_id} ''', shelving_id)

    def get_shelve_object(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves WHERE shelve_id = {shelve_id} ''', shelve_id)

    def get_item_type_object(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types WHERE item_type_type_id = {item_type_type_id} ''', item_type_id)

    def get_item_object(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items WHERE item_id = {item_id} ''', item_id)

    def get_all_rooms_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, name, description, positions FROM rooms''')

    def get_all_shelvings_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id, code, positions FROM shelves''')

    def get_all_shelves_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves''')

    def get_all_item_types_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types''')

    def get_all_items_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items''')

    def get_room_object(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM rooms WHERE room_id = {room_id} ''', room_id)

    def get_shelving_object(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id, code, positions FROM shelves WHERE shelving_id = {shelving_id} ''', shelving_id)

    def get_shelve_object(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves WHERE shelve_id = {shelve_id} ''', shelve_id)

    def get_item_type_object(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types WHERE item_type_type_id = {item_type_type_id} ''', item_type_id)

    def get_item_object(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items WHERE item_id = {item_id} ''', item_id)

    def get_room_id(room_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id FROM rooms WHERE name = {room_name} ''', room_name)

    def get_shelving_id(shelving_code: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id FROM shelvings WHERE code = {shelving_code} ''', shelving_code)

    def get_shelve_id(shelve_code: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id FROM shelves WHERE code = {shelve_code} ''', shelve_code)

    def get_item_type_id(item_type_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT item_type_id FROM item_types WHERE name = {item_type_name} ''', item_type_name)

    def get_item_id(item_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT item_id FROM items WHERE name = {item_name} ''', item_name)

    def get_shelving_by_room_id(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute("SELECT id, code, positions FROM shelvings WHERE room_id = ?", [room_id])

    # *Inserción de datos
    def insert_room(room: Room,cur: Cursor) -> bool:
        cur.execute('''INSERT INTO rooms VALUES ({room.name}, {room.description}, {room.positions}, {room.creation_date})''',
                    room.name, room.description, room.positions, room.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_shelving(shelving: Shelving, cur: Cursor) -> bool:
        cur.execute('''INSERT INTO shelvings VALUES ({shelving.room_id}, {shelving.code}, {shelving.positions}, {shelving.creation_date})''',
                    shelving.room_id, shelving.code, shelving.positions, shelving.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_shelve(shelve: Shelve, cur: Cursor) -> bool:
        cur.execute('''INSERT INTO shelves VALUES ({shelve.shelving_id}, {shelve.code}, {shelve.order}, {shelve.creation_date})''',
                    shelve.shelving_id, shelve.code, shelve.order, shelve.creation_date)
        return True if cur.lastrowid > 0 else False

    def insert_item_type(item_type: ItemType, cur: Cursor) -> bool:
        cur.execute('''INSERT INTO item_type VALUES ({item_type.name}, {item_type.description}, {item_type.positions})''',
                    item_type.name, item_type.description, item_type.positions)
        return True if cur.lastrowid > 0 else False

    def insert_item(item: Item, cur: Cursor) -> bool:
        cur.execute('''INSERT INTO item VALUES ({item.shelving_id}, {item.item_type_id}, {item.position}, {item.code}, {item.name}, {item.description}, {item.is_active}''',
                    item.shelving_id, item.item_type_id, item.position, item.code, item.name, item.description, True)
        return True if cur.lastrowid > 0 else False

    # *Actualización de datos
    def update_room(room_id: int, room: Room, cur: Cursor) -> bool:
        cur.execute('''UPDATE rooms SET name= {room.name}, description= {room.description}, positions= {room.positions} WHERE room_id= {room_id}''',
                    room.name, room.description, room.positions, room_id)
        return True if cur.lastrowid > 0 else False

    def update_shelving(shelving: Shelving, shelving_id: int, cur: Cursor) -> bool:
        cur.execute('''UPDATE shelving SET room_id= {shelving.room_id}, code= {shelving.code}, positions= {shelving.positions} WHERE shelving_id= {shelving_id}''',
                    shelving.room_id, shelving.code, shelving.positions, shelving_id)
        return True if cur.lastrowid > 0 else False

    def update_shelve(shelve: Shelve, shelve_id: int, cur: Cursor) -> bool:
        cur.execute('''UPDATE shelve SET shelve_id= {shelve.shelve_id}, code= {shelve.code}, order= {shelve.order} WHERE shelve_id= {shelve_id}''',
                    shelve.shelving_id, shelve.code, shelve.order, shelve_id)
        return True if cur.lastrowid > 0 else False

    def update_item_type(item_type: ItemType, item_type_id: int, cur: Cursor) -> bool:
        cur.execute('''UPDATE item_type SET name= {item_type.name}, description= {item_type.description}, positions= {item_type.positions} WHERE item_type_id= {item_type_id}''',
                    item_type.name, item_type.description, item_type.positions, item_type_id)
        return True if cur.lastrowid > 0 else False

    def update_item(item: Item, item_id: int, cur: Cursor) -> bool:
        cur.execute('''UPDATE item SET shelve_id= {item.shelve_id}, item_type_id= {item.item_type_id} , position= {item.position} ,name= {item.name}, description= {item.description}= {item.is_active} WHERE id= {item_id}''',
                    item.shelve_id, item.item_type_id, item.position, item.name, item.description, True, item_id)
        return True if cur.lastrowid > 0 else False

    # *Desactivacion\\activacion de datos
    def alternate_room(room_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''UPDATE room SET is_active = FALSE WHERE id= {room_id}''', room_id)
        return True if cur.lastrowid > 0 else False

    def alternate_shelving(shelving_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''UPDATE shelving SET is_active = FALSE WHERE id= {shelving_id}''', shelving_id)
        return True if cur.lastrowid > 0 else False

    def alternate_shelve(shelve_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''UPDATE shelve SET is_active = FALSE WHERE id= {shelve_id}''', shelve_id)
        return True if cur.lastrowid > 0 else False

    def alternate_item_type(item_type_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''UPDATE item_type SET is_active = FALSE WHERE id= {item_type_id}''', item_type_id)
        return True if cur.lastrowid > 0 else False

    def alternate_item(item_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''UPDATE item SET is_active = FALSE WHERE id= {item_id}''', item_id)
        return True if cur.lastrowid > 0 else False

    # *Borrado de datos
    def delete_room(room_id: int, cur: Cursor) -> bool:
        cur.execute('''DELETE FROM room WHERE id= {room_id}''', room_id)
        return True if cur.lastrowid > 0 else False

    def delete_shelving(shelving_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''DELETE FROM shelving WHERE id = {shelving_id}''', shelving_id)
        return True if cur.lastrowid > 0 else False

    def delete_shelve(shelve_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''DELETE FROM shelve WHERE id = {shelve_id}''', shelve_id)
        return True if cur.lastrowid > 0 else False

    def delete_item(item_id: int, cur: Cursor) -> bool:
        cur.execute('''DELETE FROM item WHERE id = {item_id}''', item_id)
        return True if cur.lastrowid > 0 else False

    def delete_item_type(item_type_id: int, cur: Cursor) -> bool:
        cur.execute(
            '''DELETE FROM item_type WHERE id = {item_type_id}''', item_type_id)
        return True if cur.lastrowid > 0 else False
