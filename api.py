from flask.ext.restful import reqparse, abort, Api, Resource
from flask.ext.restful import fields, marshal, marshal_with, Api

# a resource class that will be mapped to a URL
class ApiTest(Resource):
    def get(self, id):
        return test_helper_function(id)

def test_helper_function(id):
	return "Test Data {0}".format(id)
