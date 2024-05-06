from flask import Flask
from flask_cors import CORS
from extensions import db
from routes import api_bp
import os

abs_instance_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'instance')) #<--- this will be the instance directory
app = Flask(__name__, instance_path=abs_instance_path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite3'
db.init_app(app)

# enable CORS
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5173"])
app.register_blueprint(api_bp, url_prefix='/api')

with app.app_context():
    from models import Todo
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)