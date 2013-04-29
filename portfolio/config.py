class Config(object):
	""" config """

	SECRET_KEY = '01fe45sfvri39ndk'
	#: mail settings
	MAIL_SERVER = "smtp.gmail.com"
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'alving.nyc@gmail.com'
	MAIL_PASSWORD = 'brainiac86'	

	#DBUSER = 'root' # *************
	#DBPASS = '' # *************
	#DBHOST = 'localhost' # host ip or localhost
	#DBNAME = 'portfolio' # database name
	#DB = 'mysql' # sqlite / mysql/ postgresql
	#: database configuration
	#SQLALCHEMY_DATABASE_URI = DB + '://' + DBUSER + ':' + DBPASS + '@' + DBHOST + '/' +DBNAME
