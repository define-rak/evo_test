# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText)
    epithet_id = db.Column(db.Integer)


class epithets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epithet = db.Column(db.UnicodeText)