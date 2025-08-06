import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), 'cv_data.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    cursor= conn.cursor()
    return conn, cursor