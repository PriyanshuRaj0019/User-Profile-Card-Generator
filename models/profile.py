from datetime import datetime
from models import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    bio = db.Column(db.Text, nullable=False)

    image_url = db.Column(db.String(500), nullable=False)

    age = db.Column(db.Integer, nullable=False)

    occupation = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), nullable=False, unique=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Profile {self.name}>"