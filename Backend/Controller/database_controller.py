from shelvingManager.Backend.Database.database import DatabaseUtils as db
from sqlite3 import Connection

class DatabaseController:

    conn = None

    def __init__(self):
        self.conn = self.connect_to_database()
        self.create_database()
        self.conn.set_trace_callback(print)

    def connect_to_database(self):
        con = db.connect_to_db()
        return con

    def create_database(self):
        return db.create_db(self.conn)

    def close_database(self):
        db.close_db(self.conn)