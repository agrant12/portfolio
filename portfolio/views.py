from flask import render_template, url_for
from portfolio import portfolio 

@portfolio.route('/')

def home():
 	return render_template('home.html')

@portfolio.route('/about')

def about():
 	return render_template('about.html')

@portfolio.route('/contact')

def contact():
	return render_template('contact.html')

@portfolio.route('/work')

def work():
	return render_template('work.html')

@portfolio.route('/blog')

def blog():
	return render_template('blog.html')