from . import *
from datetime import datetime


record_doctor = db.Table('record_doctor',
					 db.Column('record_id', db.Integer, db.ForeignKey('records.id'), primary_key=True),
					 db.Column('doctor_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
					 )

class RecordModel(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'), index=True)
    commit_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    symptoms = db.Column(db.Text, nullable=False, default='')
    image_path = db.Column(db.String(64), nullable=False, default='')
    height= db.Column(db.Integer, nullable=False, default='')
    top = db.Column(db.Integer, nullable=False, default='')
    width = db.Column(db.Integer, nullable=False, default='')
    left = db.Column(db.Integer, nullable=False, default='')
    score = db.Column(db.Float,nullable=False)
    name = db.Column(db.String(64), nullable=False, default='')

    doctors = db.relationship('UserModel', secondary=record_doctor, backref=db.backref('records'))

    def __init__(self, username, symptoms, height, top, width, left, score, name):
        self.username = username
        self.symptoms = symptoms
        self.height = height
        self.top = top
        self.width = width
        self.left = left
        self.score = score
        self.name = name

    def add_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username)

    @classmethod
    def pagination_doctor(cls, page, per_page=3):
        return cls.query.filter_by().paginate(page,per_page=per_page)

    @classmethod
    def pagination_user(cls, page, username, per_page=3):
        return cls.query.filter_by(username=username).paginate(page,per_page=per_page)