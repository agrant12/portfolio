""" models 

create your models here
"""

from . import db


class MyTable(db.Model):
	""" Users """

	_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
