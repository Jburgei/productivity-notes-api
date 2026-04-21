from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes.auth_routes import auth_bp
from routes.note_routes import note_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(note_bp)

@app.route('/')
def home():
    return {'message': 'Productivity Notes API is running'}, 200

if __name__ == '__main__':
    app.run(debug=True)