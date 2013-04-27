from flask import Flask, render_template, url_for, redirect, request, flash
from portfolio import portfolio
from forms import ContactForm
from flask.ext.mail import Message, Mail
from . import mail
from . import twitter

@portfolio.route('/')
def home():
 	return render_template('home.html',
 		title = 'Home')

@portfolio.route('/about')
def about():
 	return render_template('about.html',
 		title = 'About')

@portfolio.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', 
				title = 'Contact', 
				form = form)
		else:
			msg = Message(form.subject.data, sender='contact@example.com', recipients=['alving.nyc@gmail.com']) 
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return render_template('contact.html',
				title = 'Contact',
				success = True,
				form = form)

	elif request.method == 'GET':	
		return render_template('contact.html',
			title = 'Contact',
			form = form)

@portfolio.route('/work')
def work():
	return render_template('work.html',
		title = 'Portfolio')

@portfolio.route('/blog')
def blog():
	return render_template('blog.html',
		title = 'Blog')