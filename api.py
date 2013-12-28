from flask.ext.restful import reqparse, abort, Api, Resource
from flask.ext.restful import fields, marshal, marshal_with
from flask.ext.mongoengine import MongoEngine
from mongoengine import NotUniqueError, DoesNotExist
from models import Test

test_fields = {
	'name': fields.String,
	'desc': fields.String,
	'active': fields.Boolean,
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, location='json')
parser.add_argument('desc', type=str, location='json')
parser.add_argument('active', type=bool, location='json')

def get_or_404(name):
	try:
		return Test.objects.get(name=name)
	except DoesNotExist as e:
	 	abort(404, message="Test {} doesn't exist: {}".format(name, e.message))


# a resource class that will be mapped to a URL
class ApiTest(Resource):
	@marshal_with(test_fields)
	def get(self, name):
		return get_or_404(name)

	def delete(self, name):
		test = get_or_404(name)
		test.delete()
		return '', 204

	@marshal_with(test_fields)
	def put(self, name):
		# update the test object
		test = get_or_404(name)
		args = parser.parse_args()
		try:
			test['name'] = args['name'] if args['name'] else test.name
			test['desc'] = args['desc'] if args['desc'] else test.desc
			test['active'] = args['active'] if args['active'] else test.active
			test.save()
			return test, 201
		except NotUniqueError as e:
			return 500, "Name is not unique: {}".format(e.message)


class ApiTestList(Resource):
	@marshal_with(test_fields)
	def get(self):
		return Test.objects.all()

	@marshal_with(test_fields)
	def post(self):
		# example POST payload: { "name": "UW", "desc": "Huskies", "active": false }
		args = parser.parse_args()
		try:
			test = Test( 
				name = args['name'], 
				desc = args['desc'], 
				active = args['active']
				)
			test.save()
			return test, 201
		except NotUniqueError as e:
			return 500, "Name is not unique: {}".format(e.message)

