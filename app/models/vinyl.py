from app import db

class Vinyl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    artist_id = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    cover_image = db.Column(db.String(100))
    onSale = db.Column(db.Boolean, default=False)
