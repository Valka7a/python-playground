import datetime

from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from flask_peewee.utils import object_list
from functools import wraps
from hashlib import md5
from peewee import *


DATABASE = 'my-blog.db'
DEBUG = True


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
    content = TextField()

    class Meta:
        order_by = ('-date_created',)


def create_tables():
    database.connect()
    database.create_tables([User, Story])

def auth_user(user):
    session['singed_in'] = True
    session['user_id'] = user.id
    session['name'] = user.first_name
    flash('Wellcome %s' % (user.first_name))

def get_current_user():
    if session.get('logged_in'):
        return User.get(User.id == session['user_id'])

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return inner

@app.route('/')
def homepage():
    stories = Story.select()
    return object_list('homepage.html', stories, 'stories')

@app.route('/story/<int:id>/')
def single_story(id):
    return 'Story: %s' % id

@app.route('/about/')
def about_page():
    return 'About'

@app.route('/create-story/')
#@login_required
def create_story():
    return 'Create-Story'

@app.route('/profile/<username>/')
#@login_required
def profile(username):
    return 'Profile: %s' % username

@app.route('/edit-story/<int:id>/')
#@login_required
def edit_story(id):
    return 'Edit: %s' % id

@app.route('/delete-story/<int:id>/')
#@login_required
def delete_story(id):
    return 'Delete: %s' % id

@app.route('/sing-up/')
def sing_up():
    return 'Sing-up'

@app.route('/sing-in/')
def sing_in():
    return 'Sing-in'

@app.route('/sing-out/')
def sing_out():
    return 'Sing-out'








if __name__ == '__main__':
    app.run()
