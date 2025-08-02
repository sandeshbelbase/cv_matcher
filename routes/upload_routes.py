import os
import sqlite3
from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename
from database.helper import get_db


conn, cursor = get_db()
upload_bp =  Blueprint('upload', __name__)
@upload_bp.route("/upload", methods=['POST'])
def upload():
    applicant_name = request.form.get('applicant_name')
    job_id = request.fom.get('job_id')
    email = request.form.get('email')
    phone = request.form.get('phone')
    cv_file = request.files.get('cv')

    if not cv_file or not cv_file.filename.endswith('.pdf'):
        return("Error:" "please upload PDF files"), 400
    
    #save the file

    filename = secure_filename(cv_file.filename)
    save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    cv_file.save(save_path)

    try:
        cursor.execute('''
            INSERT INTO cv_records(
                       applicant_name, email, phone, file_path, job_id
             VALUES(?,?,?,?,?))
        ''', ( applicant_name, email, phone, save_path, job_id))

        conn.commit()
        conn.close()

        return {"message": "Job applied Successfully."}, 200
    
    except Exception as e: 
        return {"error:" f"Database error:{str(e)}"}, 500
