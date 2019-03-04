from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields

class Movies(Document):
    movieId = fields.IntField(required=True)
    title = fields.StringField(required=True)
    genres = fields.StringField(required=True)

class Ratings(Document):
    userId = fields.IntField(required=True)
    movieId = fields.IntField(required=True)
    rating = fields.IntField(required=True)
    timestamp = fields.IntField(required=True)

class custom_ratings(Document):
    userId = fields.IntField(required=False)
    movieId = fields.IntField(required=False)
    rating = fields.IntField(required=False)
    timestamp = fields.IntField(required=False)

class Links(Document):
    movieId = fields.IntField(required=True)
    imdbId = fields.IntField(required=True)
    tmdbId = fields.IntField(required=True)

class Tags(Document):
    userId = fields.IntField(required=True)
    movieId = fields.IntField(required=True)
    tag = fields.StringField(required=True)
    timestamp = fields.IntField(required=True)
