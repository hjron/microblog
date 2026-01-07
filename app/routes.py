from flask import render_template
from app import app

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