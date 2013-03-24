from flask import Flask, render_template

import twitter

app = Flask(__name__)

@app.route('/')

def home():
 	return render_template('home.html')

@app.route('/about')

def about():
 	return render_template('about.html')
 	api = twitter.Api()
	statuses = api.GetPublicTimeline()

@app.route('/contact')

def contact():
	return render_template('contact.html')

@app.route('/work')

def work():
	return render_template('work.html')

@app.route('/blog')

def blog():
	return render_template('blog.html')

if __name__ == '__main__':
  app.run(debug=True)