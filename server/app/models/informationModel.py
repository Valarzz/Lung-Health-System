from . import *


class InformationModel(db.Model):
    __tablename__ = 'information'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'), unique=True, index=True)
    name = db.Column(db.String(64), nullable=False)
    background = db.Column(db.String(128), nullable=False)
    organization = db.Column(db.String(128), nullable=False)

    def __init__(self, username, name, background, organization):
        self.username = username
        self.name = name
        self.background = background
        self.organization = organization

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def add_information(self):
        db.session.add(self)
        db.session.commit()
