from msilib.schema import Class
from posixpath import dirname
import sqlite3
import os

from colorama import Cursor

class database:
    
    def connec_to_db():
        
        con = sqlite3.connect('/home/gragak/Code/shelvingManager/shelvingManager/Backend/database/prueba.db')

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../scripts/sql.sqlite')

        with open(filename, 'r') as file:
            data = file.read()

        return con.executescript(data)