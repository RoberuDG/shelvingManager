import sqlite3
from sqlite3 import Connection, Cursor, Error
import os
from shelvingManager.Models.item import Item
from shelvingManager.Models.item_type import ItemType

from shelvingManager.Models.room import Room
from shelvingManager.Models.shelf import Shelf
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

    def close_db(connection: Connection):
        connection.close()
        print("Conexión cerrada")

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
        return cur.execute('''SELECT * FROM rooms WHERE room_id = ? ''', [room_id])

    def get_shelving(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelvings WHERE id = ? ''', [shelving_id])

    def get_shelf(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM shelves WHERE shelve_id = ? ''', [shelve_id])

    def get_item_type(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM item_types WHERE item_type_type_id = ? ''', [item_type_id])

    def get_item(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT * FROM items WHERE item_id = ? ''', [item_id])

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
        return cur.execute('''SELECT id, name, description, positions FROM rooms WHERE id = ? ''', [room_id])

    def get_shelving_object(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, room_id, code, position, description FROM shelvings WHERE id = ? ''', [shelving_id])

    def get_shelf_object(shelve_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves WHERE id = ? ''', [shelve_id])

    def get_item_type_object(item_type_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types WHERE item_type_type_id = ? ''', [item_type_id])

    def get_item_object(item_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items WHERE item_id = ? ''', [item_id])

    def get_all_rooms_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, name, description, positions FROM rooms''')

    def get_all_shelvings_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, room_id, code, position, description FROM shelvings''')

    def get_all_shelves_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id, code, order FROM shelves''')

    def get_all_item_types_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT name, description, positions FROM item_types''')

    def get_all_items_object(cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id, item_type_id, position, name, description FROM items''')

    def get_room_id(room_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT room_id FROM rooms WHERE name = ? ''', [room_name])

    def get_shelving_id(shelving_code: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelving_id FROM shelvings WHERE code = ? ''', [shelving_code])

    def get_shelve_id(shelve_code: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT shelve_id FROM shelves WHERE code = ? ''', [shelve_code])

    def get_item_type_id(item_type_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT item_type_id FROM item_types WHERE name = ? ''', [item_type_name])

    def get_item_id(item_name: str, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT item_id FROM items WHERE name = ? ''', [item_name])

    def get_shelving_by_room_id(room_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, room_id, code, position, description FROM shelvings WHERE room_id = ?''', [room_id])

    def get_shelves_by_shelving_id(shelving_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, shelving_id, name, position FROM shelves WHERE shelving_id = ? ORDER BY position''', [shelving_id])

    def get_items_by_shelf_id(shelf_id: int, cur: Cursor) -> Cursor:
        return cur.execute('''SELECT id, shelf_id, item_type_id, position, name, description FROM items WHERE shelf_id = ? ORDER BY position''', [shelf_id])

    # *Inserción de datos
    def insert_room(room: Room,cur: Cursor, con: Connection) -> bool:
        cur.execute('''INSERT INTO rooms (name, description, positions) VALUES (?, ?, ?)''',
                    [room.name, room.description, room.positions])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def insert_shelving(shelving: Shelving, cur: Cursor, con: Connection) -> bool:
        cur.execute('''INSERT INTO shelvings (room_id, code, description, position) VALUES (?, ?, ?, ?)''',
                    [shelving.room_id, shelving.code, shelving.description, shelving.position])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def insert_shelve(shelf: Shelf, cur: Cursor, con: Connection) -> bool:
        cur.execute('''INSERT INTO shelves (shelving_id, name, position) VALUES (?, ?, ?)''',
                        [shelf.shelving_id, shelf.code, shelf.position])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def insert_item_type(item_type: ItemType, cur: Cursor, con: Connection) -> bool:
        cur.execute('''INSERT INTO item_type VALUES (?, ?, ?)''',
                    [item_type.name, item_type.description, item_type.positions])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def insert_item(item: Item, cur: Cursor, con: Connection) -> bool:
        cur.execute('''INSERT INTO item VALUES (?, ?, ?, ?, ?)''',
                    [item.shelve_id, item.item_type_id, item.position, item.name, item.description])
        con.commit()
        return True if cur.lastrowid > 0 else False

    # *Actualización de datos
    def update_room(room_id: int, room: Room, cur: Cursor, con: Connection) -> bool:
        cur.execute('''UPDATE rooms SET name= ?, description= ?, positions= ? WHERE room_id= ?''',
                    [room.name, room.description, room.positions, room_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def update_shelving(shelving: Shelving, shelving_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute('''UPDATE shelving SET room_id= ?, code= ?, positions= ? WHERE shelving_id= ?''',
                    [shelving.room_id, shelving.code, shelving.positions, shelving_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def update_shelf(shelf: Shelf, shelve_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute('''UPDATE shelf SET shelve_id= ?, code= ?, position= ? WHERE shelve_id= ?''',
                    [shelf.shelving_id, shelf.code, shelf.position, shelve_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def update_item_type(item_type: ItemType, item_type_id: int, cur: Cursor) -> bool:
        cur.execute('''UPDATE item_type SET name= ?, description= ?, positions= ? WHERE item_type_id= ?''',
                    [item_type.name, item_type.description, item_type.positions, item_type_id])
        return True if cur.lastrowid > 0 else False

    def update_item(item: Item, item_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute('''UPDATE item SET shelve_id= ?, item_type_id= ?, position= ?,name= ?, description= ? WHERE id= ?''',
                    [item.shelve_id, item.item_type_id, item.position, item.name, item.description, item_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    # *Borrado de datos
    def delete_room(room_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute('''DELETE FROM room WHERE id= ?''', [room_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def delete_shelving(shelving_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute(
            '''DELETE FROM shelving WHERE id = ?''', [shelving_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def delete_shelve(shelve_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute(
            '''DELETE FROM shelf WHERE id = ?''', [shelve_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def delete_item(item_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute('''DELETE FROM item WHERE id = ?''', [item_id])
        con.commit()
        return True if cur.lastrowid > 0 else False

    def delete_item_type(item_type_id: int, cur: Cursor, con: Connection) -> bool:
        cur.execute(
            '''DELETE FROM item_type WHERE id = ?''', [item_type_id])
        con.commit()
        return True if cur.lastrowid > 0 else False
