from . import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    notes = db.relationship('Note', backref='user', cascade='all, delete-orphan')

    # Prevent reading password
    @property
    def password(self):
        raise AttributeError('Password is not readable')

    # Set password
    @password.setter
    def password(self, plain_password):
        self.password_hash = generate_password_hash(plain_password).decode('utf-8')

    # Authenticate user
    def authenticate(self, plain_password):
        return check_password_hash(self.password_hash, plain_password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }