from flask_restful import Resource
from app import auth
from app import db
from .. import app, socketio
from flask_socketio import emit, join_room, leave_room

from ..models.userModel import UserModel
from ..models.informationModel import InformationModel
from ..models.recordModel import RecordModel
from ..models.chatModel import ChatModel

from flask import json, jsonify, request, abort, g


@auth.verify_token
def verify_token(token):
    user = UserModel.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True