from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ronnyaldo'}
    posts = [
        {
            'author': {'username': 'john'},
            'body': 'nice day in mpls'
        },
        {
            'author': {'username': 'susan'},
            'body': 'can\'t wait for new season of Pitt!!'
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
