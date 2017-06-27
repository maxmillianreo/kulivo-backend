from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'tbl_user'

    userEmail = db.Column(db.String(60), index=True, unique=True, primary_key=True)
    userFullname = db.Column(db.String(160))
    password = db.Column(db.String(128))

    def __init__(self, email, userfullname):
        self.userEmail = username
        self.userFullname = userfullname

    def __str__(self):
        return '%s' % self.userEmail

    @property
    def getList(self):
    	return {
           'email'   : self.userEmail,
           'fullname': self.userFullname
       }