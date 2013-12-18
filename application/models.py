from application import db

ROLE_USER  = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __init__(self, nickname, email, role = ROLE_USER):
    	self.nickname = nickname
    	self.email = email
    	self.role  = role

    def is_authenticated(self):
    	return True

    def is_active(self):
    	return True

    def is_anonymous(self):
	    return False

    def get_id(self):
    	return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body, timestamp, user_id):
    	self.body = body
    	self.timestamp = timestamp
    	self.user_id = user_id
    def __repr__(self):
        return '<Post %r>' % (self.body)



