from datetime import datetime, timezone, timedelta
from app import app, db
from app.models import User, Post

ac = app.app_context()
ac.push()

# users
u1 = User(username='ron', email='ron@ron.com')
u2 = User(username='susan', email='susan@ron.com')
u3 = User(username='mary', email='mary@ron.com')
u4 = User(username='joe', email='joe@ron.com')
u1.set_password('pass')
u2.set_password('pass')
u3.set_password('pass')
u4.set_password('pass')

db.session.add_all([u1, u2, u3, u4])
db.session.commit()

# posts
for user in [u1, u2, u3, u4]:
    for j in range(1, 11):
        this_post = Post(body=f'post number {j} from {user.username}', 
                        author=user,
                        timestamp=datetime.now(timezone.utc) +
                         timedelta(seconds=j))
        db.session.add(this_post)
    db.session.commit()

# followers
u1.follow(u2)
u1.follow(u4)
u2.follow(u3)
u2.follow(u1)
u3.follow(u4)
db.session.commit()

ac.pop()
