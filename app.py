from flask import Flask
from routes.upload_routes import upload_bp
from database.db import init_db
app = Flask(__name__)
init_db()
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)