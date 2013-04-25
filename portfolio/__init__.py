from flask import Flask
from flask.ext.mail import Message, Mail

mail = Mail()

portfolio = Flask(__name__)

portfolio.secret_key = 'testkey'

portfolio.config["MAIL_SERVER"] = "smtp.gmail.com"
portfolio.config["MAIL_PORT"] = 465
portfolio.config["MAIL_USE_SSL"] = True
portfolio.config["MAIL_USERNAME"] = 'contact@example.com'
portfolio.config["MAIL_PASSWORD"] = 'your-password'

mail.init_app(portfolio)

from portfolio import views