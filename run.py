from flask import Flask
from flask.ext.restful import Api as FlaskRestful
from api import ApiTest
 
# our application instance
zoo = Flask(__name__)
# our api instance
flask_api = FlaskRestful(zoo)

# TODO, put into a seperate file, usually named routes.py
flask_api.add_resource(ApiTest, '/api/test/<int:id>')

if __name__ == '__main__':
    zoo.run(debug=True)