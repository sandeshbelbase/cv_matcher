import os
from werkzeug.utils import secure_filename
from models.cv_model import CVRecord

class CVService:
    def __init__(self, upload_folder):
        self.upload_folder=upload_folder

    def save_file(self, cv_file):
        filename = secure_filename(cv_file.filename)
        save_path = os.path.join(self.upload_folder, filename)
        cv_file.save(save_path)
        return save_path
    
    def process_upload(self, conn, applicant_name, email, phone, job_id, cv_file):
        save_path = self.save_file(cv_file)
        cv_record = CVRecord(applicant_name, email, phone, job_id, save_path)
        is_valid, error = cv_record.validate()
        if not is_valid:
            return False, error
        cv_record.save_to_db(conn)
        return True, f"Job applied successfully for {applicant_name}"


