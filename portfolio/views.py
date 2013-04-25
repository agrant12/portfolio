from flask import render_template, url_for, redirect, request, flash
from portfolio import portfolio
from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("Name", [validators.Required("Please Enter Your Name")])
	email = TextField("Email", [validators.Required("Please Enter Your Email"), validators.Email("Please Eneter Your Email")])
	subject = TextField("Subject", [validators.Required("Please Enter A Subject")])
	message = TextAreaField("Message", [validators.Required("Please Enter a Subject")])
	submit = SubmitField("Send")

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
				form=form)
		else:
			msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com']) 
			msg.body = """
				From: %s <%s>
				%s""" % (form.name.data, form.email.data, form.message.data)
			return 'Form Posted.'

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