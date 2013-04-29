from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("Name", [validators.Required("Please Enter Your Name")])
	email = TextField("Email", [validators.Required("Please Enter Your Email"), validators.Email("Please Eneter Your Email")])
	subject = TextField("Subject", [validators.Required("Please Enter A Subject")])
	message = TextAreaField("Message", [validators.Required("Please Enter a Subject")])
	submit = SubmitField("Send")

class PostForm(Form):
	title = TextField("Title", [validators.Required("Please Enter A Title")])
	body = TextAreaField("Body", [validators.Required("Please Enter Text")])