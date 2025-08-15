import sqlite3
import os

DB_PATH = os.path.join(os.getcwd(), "cv_data.db")

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

    # lets store the parsed CV
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parsed_cv (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cv_id INTEGER NOT NULL,
                   parsed_text TEXT NOT NULL,
                   FOREIGN KEY (cv_id) REFERENCES cv_records(id) ON DELETE CASCADE
                  )
    ''')

    conn.commit()
    conn.close()

