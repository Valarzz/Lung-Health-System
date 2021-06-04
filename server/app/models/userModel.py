from . import *


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(10), default='user')

    information = db.relationship('InformationModel', backref='user')

    def __init__(self, username, user_type= 'user'):
        self.username = username
        self.user_type = user_type

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def generate_auth_token(self, expiration=3600):
        s = Serializer(app.config['SECRET_KEY'], expiration)
        return s.dumps({'id':self.id}).decode("ascii")

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = UserModel.query.get(data['id'])
        return user

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def add_user(self):
        db.session.add(self)
        db.session.commit()
