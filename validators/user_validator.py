import re
def valid_mail(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def valid_phone(phone):
    pattern = r'^0\d{9}$'
    return re.match(pattern, phone)