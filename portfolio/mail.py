from flask.ext.mail import Message, Mail
from portfolio import portfolio

class MailSetting():

	mail = Mail()

	portfolio.secret_key = 'development key'

	portfolio.config["MAIL_SERVER"] = "smtp.gmail.com"
	portfolio.config["MAIL_PORT"] = 465
	portfolio.config["MAIL_USE_SSL"] = True
	portfolio.config["MAIL_USERNAME"] = 'alving.nyc@gmail.com'
	portfolio.config["MAIL_PASSWORD"] = 'brainiac86'

	mail.init_app(portfolio)