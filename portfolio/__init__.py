""" init """

from flask import Flask
from forms import ContactForm
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail
from flask_oauth import OAuth

from .config import Config

portfolio = Flask(__name__)

portfolio.config.from_object(Config)

mail = Mail()
mail.init_app(portfolio)

oauth = OAuth()
twitter = oauth.remote_app('twitter',
		base_url='http://api.twitter.com/1/',
		request_token_url='https://api.twitter.com/oauth/request_token',
		access_token_url= 'https://api.twitter.com/auth/access_token',
		authorize_url='https://api.twitter.com/oauth/authenticate',
		consumer_key='<my key>',
		consumer_secret='<my secret>'
		)

db = SQLAlchemy(portfolio)
from .models import MyTable
db.create_all()


from portfolio import views