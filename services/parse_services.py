import sqlite3
import os
from database.db import DB_PATH
from PyPDF2 import PdfReader
from models.parsed_cv import ParsedCV
class cvParser:
    def __init__(self):
        pass
    
    def parse_cv(self, cv_id, file_path):
        text_content=""
        if file_path.lower().endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = PdfReader(f) 
                for page in reader.pages:
                    text_content += page.extract_text() or ""
        else:
            raise ValueError("File type is not in pdf.")

        parsed_cv = ParsedCV(cv_id=cv_id,parsed_text=text_content)
        parsed_cv.save()

        return True, "CV parsed successfully."