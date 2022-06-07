from shelvingManager.Backend.Database.database import DatabaseUtils as db
from sqlite3 import Connection

class DatabaseController:
    def connect_to_database():
        return db.connect_to_db()

    def create_database(con: Connection):
        return db.create_db(con)