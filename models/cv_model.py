import re

class CVRecord:
    def __init__(self, applicant_name, email, phone, file_path, job_id):
        self.applicant_name = applicant_name
        self.email = email
        self.phone = phone
        self.file_path = file_path
        self.job_id = job_id


    def valid_mail(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, self.email) is not None

    def valid_phone(self):
        pattern = r'^0\d{9}$'
        return re.match(pattern, self.phone) is not None
    
    def validate(self):
        if not self.applicant_name:
            return False, "Applicant name is required."
        if not self.valid_mail:
            return False, "Applicant email is required"
        if not self.valid_phone:
            return False, "Applicant phone isrequired"
        return True, None
        
    def save_to_db(self, conn):
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cv_records(applicant_name, email, phone, file_path, job_id)
            values(?, ?, ?, ?, ?)             
        ''', (self.applicant_name, self.email, self.phone, self.file_path, self.job_id))
        cursor.close()
        conn.close()