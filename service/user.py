from crypt import methods
from itertools import tee
import json
from flask import Response, Blueprint, request
from parser.user import *
from repository.user import *
from utils.response import *

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route('/user', methods=['POST'])
def Register():
    user = ParseUser(request)

    success = RegisterRepo(user)
    if success == True:
        return SuccessInsertResponse()
    else:
        return FailInsertResponse()    

# @users_blueprint.route('/user', methods=[])
# def register():


