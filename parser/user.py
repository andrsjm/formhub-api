import uuid
from entity.user import User
from flask import request
from utils.utils import *

def ParseUser(request):
    data = request.form
    id = str(uuid.uuid4())
    password = GetHashPassword(data["password"])
    user = User(id, data["username"], data["email"], password)
    return user



