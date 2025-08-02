import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "cv_data.dv")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cv_records (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   job_id INTEGER NOT NULL,
                   applicant_name TEXT NOT NULL,
                   email TEXT NOT NULL,
                   phone TEXT NOT NULL,
                   file_path TEXT NOT NULL,
                   upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )               
    ''')

    conn.commit()
    conn.close()

