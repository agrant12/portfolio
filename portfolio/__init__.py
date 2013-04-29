""" init """

from flask import Flask
from forms import ContactForm
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail
from flask_oauth import OAuth
import twitter

from .config import Config

POSTS_PER_PAGE = 5

portfolio = Flask(__name__)

portfolio.config.from_object(Config)

mail = Mail()
mail.init_app(portfolio)

#api = twitter.api(
#		base_url='http://api.twitter.com/1/',
#		request_token_url='https://api.twitter.com/oauth/request_token',
#		access_token_url= 'https://api.twitter.com/auth/access_token',
#		authorize_url='https://api.twitter.com/oauth/authenticate',
#		consumer_key='D58jrZsvlnoBT3WybeaTSA',
#		consumer_secret='8HF72PpXL2SeHqI5oKkX056WruYeo8RUGfutyoGg0',
#		access_token='129943342-PyiqIzZ34o315ZvhADLTjYaPHmdj47xSarzXArBL'
#		)

db = SQLAlchemy(portfolio)
from .models import MyTable
db.create_all()


from portfolio import views