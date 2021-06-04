from . import *
from datetime import datetime
from sqlalchemy import or_, and_


class ChatModel(db.Model):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey("records.id"), nullable = False, index=True)
    receiver = db.Column(db.String(64), db.ForeignKey('users.username'), index=True)
    sender = db.Column(db.String(64), db.ForeignKey('users.username'), index=True)
    commit_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False, default='')

    def __init__(self, record_id, receiver, sender, content):
        self.record_id = record_id
        self.receiver = receiver
        self.sender = sender
        self.content = content

    def add_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, record_id):
        return cls.query.filter_by(record_id=record_id).first()

    @classmethod
    def find_chat(cls, username, record_id):
        return cls.query.filter(and_(cls.record_id==record_id, or_(cls.sender==username, cls.receiver==username))).order_by(ChatModel.commit_time)