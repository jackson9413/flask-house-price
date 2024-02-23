from application import db
from application import app
from datetime import datetime

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_bedrooms = db.Column(db.Integer, nullable=False)
    num_bathrooms = db.Column(db.Integer, nullable=False)
    sqft_living = db.Column(db.Integer, nullable=False)
    sqft_above = db.Column(db.Integer, nullable=False)
    sqft_basement = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __str__(self):
        return f'House {self.id}'
    
    