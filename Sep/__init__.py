from .models import *
# from .models1 import *
from .forms import *
from .api import api
from .mail import mail,ma
from .admin import admin,redirect,url_for
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from .create_db import create
from .tools import generate
def create_app(config):
	app=Flask(__name__)
	app.config.from_object(config)


	#blueprints
	app.register_blueprint(api)
	app.register_blueprint(admin)
	app.register_blueprint(ma)
	# app.config['SQLALCHEMY_BINDS']={'recovery':"sqlite:///test.db"}
	@app.route('/',methods=['GET'])
	def home():
		return redirect(url_for('api.login'))

	#init_app
	db.init_app(app)
	mail.init_app(app)
	Bootstrap(app)
	CORS(app)
	# sysAdmin.init_app(app)

	return app
