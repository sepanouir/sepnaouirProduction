from flask import request,Blueprint,jsonify,render_template
from flask_mail import Mail, Message as Msg
from .models import *
import datetime
mail=Mail()
ma=Blueprint('ma','__name__',url_prefix='/mail')
def conv(o):
	T=['jan', 'fév', 'mars', 'avr', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc']
	return "{} {}".format(o.day, T[o.month-1])


# @ma.route('/send_email/<email>/<url>/<check>',methods=['GET'])
def send_email(email,url,check):
	try :
		msg = Msg("Bienvenue dans l'application SEPanouir", sender='sepanouir.admin@gmail.com', recipients=[email])
		msg.html = render_template('mailConfirmation.html',code=check,email=email,url=url)
		mail.send(msg)
		return True #jsonify({'message':True})
	except:
		return False #jsonify({'message':False})


@ma.route('/send_email/activity/<tpe>/<user_id>/<activity_id>',methods=['GET'])
def send_email_Activities(tpe,user_id,activity_id):
	return send_email_Activity(tpe, user_id, activity_id)


def send_email_Activity(tpe,user_id,activity_id):
	act=Activity.getActivity(activity_id)
	user=User.getUser(user_id)
	print(user)
	typ={"ext":" Annulation de la réservation pour l’activité du "+act.name+" prévue le "+conv(act.date),"ent":"Confirmation de réservation SEPanouir"}
	msg = Msg(typ[tpe], sender='sepanouir.admin@gmail.com', recipients=[user.email])
	# msg.body = f"L'application sepanouir"
	msg.html = render_template('mailActivity.html',user=user,act=act,type=tpe,time=str(datetime.datetime.utcnow().date()),str=str)
	mail.send(msg)
	return jsonify({'message':True})


@ma.route('/send_email_contact/<email>',methods=['GET'])
def send_contact(email):
	msg = Msg('Sepanouir Contact', sender='sepanouir.admin@gmail.com', recipients=[email])
	msg.html = render_template('mailContact.html')
	mail.send(msg)
	return jsonify({'message':True})

def send_Res_med(email):
	msg = Msg('Sepanouir Contact', sender='sepanouir.admin@gmail.com', recipients=[email])
	msg.html = render_template('mailResmed.html')
	mail.send(msg)
	return jsonify({'message':True})
