from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_login import UserMixin
from .. import db, app
from flask import json, jsonify, request, abort, g

from .userModel import UserModel
from .informationModel import InformationModel
from .recordModel import RecordModel, record_doctor
from .chatModel import ChatModel