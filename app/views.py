from app import flaskapp
from app.models import User
from flask.json import jsonify

@flaskapp.route('/')
def index():
	return 'Hello World!'

@flaskapp.route('/home')
def home():
	return 'This is Home!'

@flaskapp.route('/getUser')
def getUser():
	userlist = User.query.all()
	userfirst = User.query.first()
	# return jsonify(data=[i.getList for i in userlist])
	return jsonify(data=[userfirst.getList])