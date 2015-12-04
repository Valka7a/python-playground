import datetime

from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from flask_peewee.utils import object_list, get_object_or_404
from functools import wraps
from hashlib import md5
from peewee import *


DATABASE = 'my-blog.db'
DEBUG = True
SECRET_KEY = 'siakshdai213o2hksaiuo94&*-=1273kn'


app = Flask(__name__)
app.config.from_object(__name__)


database = SqliteDatabase(DATABASE)


class BaseModel(Model):

    date_created = DateTimeField(default = datetime.datetime.now)
    date_updated = DateTimeField()

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)


class User(BaseModel):
    username = CharField(unique = True)
    password = CharField()
    first_name = CharField(max_length = 50)
    last_name = CharField(max_length = 50)
    email = CharField()

    class Meta:
        order_by = ('username',)

    def gravatar_url(self, size = 80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)


class Story(BaseModel):
    user = ForeignKeyField(User)
    title = CharField()
    content = TextField()

    class Meta:
        order_by = ('-date_created',)


def create_tables():
    database.connect()
    database.create_tables([User, Story])

def hash_password(password):
    return md5(password.encode('utf-8')).hexdigest()

def auth_user(user):
    session['signed_in'] = True
    session['user_id'] = user.id
    session['name'] = user.first_name
    flash('Wellcome %s' % (user.first_name))

def get_current_user():
    if session.get('signed_in'):
        return User.get(User.id == session['user_id'])

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('signed_in'):
            return redirect(url_for('sign_in'))
        return f(*args, **kwargs)
    return inner

"""
     @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
"""
@app.route('/')
def homepage():
    stories = Story.select()
    return object_list('homepage.html', stories, 'stories')

@app.route('/about/')
def about_page():
    render_template('about.html')

@app.route('/create-story/', methods = ['GET', 'POST'])
@login_required
def create_story():
    user = get_current_user()
    if request.method == 'POST' and request.form['content']:
        story = Story.create(
            user = user,
            title = request.form['title'],
            content = request.form['content']
        )
        flash('You\'r story has been created')
        return redirect(url_for('single_story', id = story.id))

    return render_template('create-story.html')

@app.route('/story/<int:id>/')
def single_story(id):
    story = get_object_or_404(Story, Story.id == id)
    user = get_object_or_404(User, User.id == story.user_id)

    return render_template('single-story.html', story = story, user = user)

@app.route('/edit-story/<int:id>/')
#@login_required
def edit_story(id):
    return 'Edit: %s' % id

@app.route('/delete-story/<int:id>/', methods = ['GET'])
@login_required
def delete_story(id):
    user = get_current_user()
    story = get_object_or_404(Story, Story.id == id, Story.user == user)
    story.delete_instance()
    flash('You\'r story has been deleted')
    return redirect(url_for('homepage'))

@app.route('/sign-up/', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST' and request.form['username']:
        try:
            with database.transaction():
                user = User.create(
                    username = request.form['username'],
                    password = hash_password(request.form['password']),
                    email = request.form['email'],
                    first_name = request.form['first_name'],
                    last_name = request.form['last_name']
                )

            auth_user(user)
            return redirect(url_for('homepage'))

        except IntegrityError:
            flash('That username is already taken.')

    return render_template('sign-up.html')

@app.route('/sign-in/', methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST' and request.form['username']:
        try:
            user = User.get(
                username = request.form['username'],
                password = request.form['password'])
        except User.DoesNotExist:
            flash('The password entered is incorrect')
        else:
            auth_user(user)
            return redirect(url_for('homepage'))

    return render_template('sign-in.html')

@app.route('/sign-out/')
#@login_required
def sign_out():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/profile/<username>/')
#@login_required
def profile(username):
    user = get_object_or_404(User, User.username == username)

    return render_template('profile.html', user = user)

@app.route('/profile/<username>/edit')
@login_required
def profile_edit(username):
    user = get_object_or_404(User, User.username == username)

    return render_template('profile-edit.html')

@app.context_processor
def _inject_user():
    return {'current_user': get_current_user()}




if __name__ == '__main__':
    app.run()
