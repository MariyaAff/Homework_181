from marshmellow import Schema, fields

from setup_db import db

from dao.model.director import DirectorSchema
from dao.model.genre import GenreSchema

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(255)
    description = fields.Str(255)
    trailer = fields.Str(255)
    year = fields.Int()
    rating = fields.Float()
    director = fields.Pluck(DirectorSchema, "name")
    genre = fields.Pluck(GenreSchema, "name")