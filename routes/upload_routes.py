import os
import sqlite3
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
from database.helper import get_db
from services.cv_services import CVService

upload_bp =  Blueprint('upload', __name__)
@upload_bp.route("/upload", methods=['POST'])
def upload():
    cv_service = CVService(upload_folder=current_app.config['UPLOAD_FOLDER'])
    conn, cursor = get_db()
    applicant_name = request.form.get('applicant_name')
    job_id = request.form.get('job_id')
    email = request.form.get('email')
    phone = request.form.get('phone')
    cv_file = request.files.get('cv')
    if not cv_file or not cv_file.filename.endswith('.pdf'):
        return("Error:" "please upload PDF files"), 400
    #save the file

    success, message = cv_service.process_upload(conn, applicant_name, email, phone, job_id, cv_file)
    conn.close()

    if not success:
        return jsonify({"error": message}), 400

    return jsonify({"message": message}), 200
