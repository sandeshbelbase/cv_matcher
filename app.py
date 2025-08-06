from flask import Flask
import os
from routes.upload_routes import upload_bp
from database.db import init_db
app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_cvs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
init_db()
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)
    print("hello")