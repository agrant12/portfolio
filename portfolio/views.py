from flask import Flask, render_template, url_for, redirect, request, flash
from portfolio import portfolio
from forms import ContactForm, PostForm
from flask.ext.mail import Message, Mail
#from portfolio import db, oid, babel
from . import mail
from . import POSTS_PER_PAGE
from twitter import *
import oauth2 as OAuth

#@lm.user_loader
#def load_user(id):
#    return User.query.get(int(id))

#@portfolio.before_request
#def before_request():
#    g.user = current_user
#    if g.user.is_authenticated():
#        g.user.last_seen = datetime.utcnow()
#        db.session.add(g.user)
#        db.session.commit()
#        g.search_form = SearchForm()
#    g.locale = get_locale()

#@portfolio.after_request
#def after_request(response):
#    for query in get_debug_queries():
#        if query.duration >= DATABASE_QUERY_TIMEOUT:
#            app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (query.statement, query.parameters, query.duration, query.context))
#    return response

@portfolio.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@portfolio.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@portfolio.route('/')
def home():
 	return render_template('home.html',
 		title = 'Home')

@portfolio.route('/about')
def about():
	consumer_key = "D58jrZsvlnoBT3WybeaTSA"
	consumer_secret = "8HF72PpXL2SeHqI5oKkX056WruYeo8RUGfutyoGg0"
	access_key = "129943342-PyiqIzZ34o315ZvhADLTjYaPHmdj47xSarzXArBL"
	access_secret = "CBGTRIdV7du0O4kfYE2lUm4LNkT3ryafvbX2A7Iqd0"

	# create twitter API object
	#auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
	#twitter = Twitter(auth = auth)

	# request my home timeline
	# twitter API docs: https://dev.twitter.com/docs/api/1/get/statuses/home_timeline
	#statuses = twitter.statuses.home_timeline(count = 1)

	# loop through each of my statuses, and print its content
	#for status in statuses:
	#	print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])
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
			msg = Message(form.subject.data, sender='alving.nyc@gmail.com', recipients=['alving.nyc@gmail.com']) 
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

#@portfolio.route('/blog', methods = ['GET', 'POST'])
#@portfolio.route('/blog/<init:page>', methods = ['GET', 'POST'])
#def blog(page = 1):
#	posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
#	return render_template('blog.html',
#		title = 'Blog',
#		posts = posts)

@portfolio.route('/admin', methods = ['GET', 'POST'])
@portfolio.route('/admin/<int:page>', methods = ['GET', 'POST'])
#@login_required
def admin(page = 1):
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body = form.post.data,
            timestamp = datetime.utcnow(),
            author = g.user)
        db.session.add(post)
        db.session.commit()
        flash(gettext('Your post is now live!'))
        return redirect(url_for('index'))
    posts = g.user.followed_posts().paginate(page, POSTS_PER_PAGE, False)
    return render_template('admin.html',
        title = 'Admin',
        form = form,
        posts = posts)