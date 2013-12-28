from mongoengine import Document, StringField, FloatField, IntField, BooleanField

class Test(Document):
	name = StringField()
	desc = StringField()
	active = BooleanField()

	meta = {
		'indexes': ['name'],
		'unique': True,
	}
