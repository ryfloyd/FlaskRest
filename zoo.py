import os
from flask import Flask
from flask.ext.restful import Api as FlaskRestful
from flask.ext.mongoengine import MongoEngine
from api import ApiTest, ApiTestList
 
# our application instance
zoo = Flask(__name__)

# load the settings
zoo.config.from_object('local_settings')

# configure the MongoDB
db = MongoEngine()
db.init_app(zoo)

# our api instance
flask_api = FlaskRestful(zoo)

# define the listening URLs
flask_api.add_resource(ApiTest, '/api/test/<string:name>')
flask_api.add_resource(ApiTestList, '/api/test/')

if __name__ == '__main__':
    zoo.run(
    	debug=zoo.config['DEBUG'],
    	port = zoo.config['PORT'],
    	use_reloader = zoo.config['USE_RELOADER']
    	)