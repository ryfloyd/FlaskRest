import os

# Determine if this is a dev, staging or prod env
if not os.environ.get('EC2-ENV'):
	SERVER_NAME = '127.0.0.1:8100'
	
	MONGO_HOST = 'localhost'
	MONGO_PORT = 27017
	MONGO_USERNAME = ''
	MONGO_PASSWORD = ''
	MONGO_DBNAME = 'zoo'
elif os.environ['EC2-ENV'] == 'STAGING':
	SERVER_NAME = 'zoo-staging.servers.thezebra.com'

	MONGO_HOST = 'db-server'
	MONGO_PORT = 27017
	MONGO_USERNAME = ''
	MONGO_PASSWORD = ''
	MONGO_DBNAME = 'zoo'	
elif os.environ['EC2-ENV'] == 'PROD':
	SERVER_NAME = 'zoo.thezebra.com'

	MONGO_HOST = 'db-server'
	MONGO_PORT = 27017
	MONGO_USERNAME = ''
	MONGO_PASSWORD = ''
	MONGO_DBNAME = 'zoo'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

test = {
	'schema': {
		'objectID': {
			'type': 'string',
			'minlength': 48,
			'maxlength': 48,
			'required': True,
			'unique': True,
		},
		'last_modified': {
			'type': 'datetime',
		}
	}
}

DOMAIN = {
    'test': test,
}




