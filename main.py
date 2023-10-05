from app import *
from flask_restful import Api

from app.routes import routes

if __name__ == "__main__":
    api = Api(app)
    routes()
    app.run(debug=True, port=8000)
    

