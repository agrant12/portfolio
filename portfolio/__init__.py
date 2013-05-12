""" init """

from flask import Flask
from forms import ContactForm
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Message, Mail

from .config import Config

POSTS_PER_PAGE = 5

portfolio = Flask(__name__)

portfolio.config.from_object(Config)

mail = Mail()
mail.init_app(portfolio)

db = SQLAlchemy(portfolio)
from .models import MyTable
db.create_all()


from portfolio import views