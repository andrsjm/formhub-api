from app import app
from service.user import users_blueprint
def routes():
    app.register_blueprint(users_blueprint)
