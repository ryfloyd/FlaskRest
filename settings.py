import os

# Determine if this is a dev, staging or prod env
if not os.environ.get('EC2-ENV', False):
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
else:
	raise KeyError




