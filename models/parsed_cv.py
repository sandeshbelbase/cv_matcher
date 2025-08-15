import sqlite3
class ParsedCV:
    def _init_(self, id, cv_id, parsed_text):
        self.id = id
        self.cv_id = cv_id
        self.parsed_text = parsed_text
    
    def save(self, conn):
        cursor= conn.cursor
        cursor.execute('''
            INSERT INTO TABLE parsed_cv(cv_id, parsed_text)
            VALUES(?, ?)
        ''', (self.cv_id, self.parsed_text))
        conn.commit()
        conn.close()