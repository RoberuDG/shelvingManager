from shelvingManager.Backend.Database.database import DatabaseUtils as db
from sqlite3 import Connection

class DatabaseController:
    def connect_to_database():
        con = db.connect_to_db()
        con.set_trace_callback(print)
        return con.cursor()

    def create_database(con: Connection):
        return db.create_db(con)