from .models import *
from flask import request,Blueprint,jsonify,send_file,redirect,url_for,render_template,session,Response
from sqlalchemy import func
import datetime
from io import BytesIO
from itertools import groupby
# from .mail import send_email_Activity,send_contact,send_Res_med
from .mail import send_email
from .cities import data
from .forms import *
import jwt
import os
from werkzeug.security import generate_password_hash, check_password_hash
from config import ProductionConfig
from functools import wraps
import csv
from werkzeug.utils import secure_filename
from .tools import generate, check_email
api=Blueprint('api','__name__',url_prefix='/api')
attend='attend'
actif='actif'



def Try(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		try:
			return f(*args, **kwargs)
		except Exception as e:
			return jsonify([])
	return wrapper

def token_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		if not token:
			return jsonify({'message' : 'Token is missing!'}), 401
		try: 
			data = jwt.decode(token,ProductionConfig.SECRET_KEY, algorithms=["HS256"])
		except:
			return jsonify({'message' : 'Token is invalid!'}), 401
		return Try(f(*args, **kwargs))

	return wrapper









def conv(o):
	T=['jan', 'fév', 'mars', 'avr', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc']
	return "{} {}".format(o.day, T[o.month-1])
def conv1(o):
	return "{}/{}/{}".format(o.day,o.month,o.year)

def conv_to_date(d):
	t=[int(i) for i in d.split('/')]
	return datetime.date(t[2], t[1], t[0])


@api.route('/logout',methods=['GET','POST'])
def logout():
	session.pop('admin')
	return redirect(url_for('sep_admin.Home'))


@api.route('/login/<var>',methods=['GET','POST'])
@api.route('/login',methods=['GET','POST'])
def login(var=None):
	form = Login()
	if request.method=='POST':
		if form.validate_on_submit():
			if form.isValid():
				if var=='update' :
					session['update']=True
					return redirect(url_for('api.update'))
				else:
					session['admin']=True
					return redirect(url_for('sep_admin.Home'))
			else :
				print("admin not found")
				return render_template('login.html',form=form,err=True)
	if form.isEmpty():
		# add token to session
		session['register']=True
		return redirect(url_for('api.register'))
	if var == 'update':
		return render_template('login.html',form=form,err=False,update=True,action="/api/login/update")
	return render_template('login.html',form=form,err=False,update=False,action="/api/login")

@api.route('/register',methods=['GET','POST'])
def register():
	if not('register' in session):
		return redirect(url_for('api.login'))
	form = Register()
	if request.method=='POST':
		if form.validate_on_submit():
			user = Admin(email=form.email.data,password=form.password.data)
			print(user)
			db.session.add(user)
			db.session.commit()
			session.pop('register')			
			return redirect(url_for('api.login'))
	return render_template('register.html',form=form)

@api.route('/update',methods=['GET','POST'])
def update():
	if not('update' in session):
		return redirect(url_for('api.login'))
	form = Update()
	if request.method=='POST':
		if form.validate_on_submit():
			newUser = Admin(email=form.email.data,password=form.password.data)
			user = Admin.query.first()
			user.email=newUser.email
			user.password=newUser.password
			db.session.commit()	
			session.pop('update')		
			return redirect(url_for('api.login'))
	return render_template('update.html',form=form)







 # *************************** activite handler *****************************

@api.route('/submit_att',methods=['POST'])
def submit_att():
	data = request.get_json(force=True)
	user_id=User.getUser(data['user_id']).id
	activity_id=Activity.getActivity(data['activity_id']).id
	if Activity_user.query.filter_by(user_id=user_id,activity_id=activity_id,state=attend).all():
		return jsonify({'message' : 'activite_user_attend has been exist'})
	db.session.add(Activity_user(user_id=user_id,activity_id=activity_id,state=attend))
	db.session.commit()
	return jsonify({'message' : 'New activite_user_attend created'})

@api.route('/test')
def test():
	# Le dimanche du bien-être
	acts = Activity.query.all()
	act=acts[1]
	print(act.name)
	Aus = Activity_user.query.filter_by(activity_id=act.id,state=actif).all()
	for i in Aus:
		print(i.rank,i.state,User.query.filter_by(id=i.user_id).first().email)
	return jsonify({'message':True})

@api.route('/submit_act',methods=['POST'])
def submit_act():
	data = request.get_json(force=True)		
	user_id=User.getUser(data['user_id']).id
	ac=Activity.getActivity(data['activity_id'])
	if Activity_user.query.filter_by(user_id=user_id,activity_id=ac.id,state=actif).all():
		return jsonify({"message":"activite_user_actif has been exist"})
	au=Activity_user(user_id=user_id,activity_id=ac.id,state=actif)
	print('au.rank  :',au.rank)
	print('ac.members :',ac.members)
	print('au.len_activity() :',au.len_activity())
	if au.len_activity() >=ac.members :
		au=Activity_user(user_id=user_id,activity_id=ac.id,state=attend)

	db.session.add(au)
	db.session.commit()
	# if au.state==actif:

		# return redirect(url_for('ma.send_email_Activities',tpe='ent',user_id=data['user_id'],activity_id=data['activity_id']))
	return jsonify({"message":"seccus"})




@api.route('/exit_att/<user_id>/<activity_id>',methods=['DELETE'])
def exit_att(user_id,activity_id):
	user_id=User.getUser(user_id).id
	activity_id=Activity.getActivity(activity_id).id
	au=Activity_user.query.filter_by(user_id=user_id, activity_id=activity_id,state=attend).first()
	if au :
		db.session.delete(au)
		db.session.commit()
		return jsonify({'message' : 'activite_user_attend deleted!'})
	return jsonify({'message':'user not found'})

@api.route('/exit_act/<user_id>/<activity_id>',methods=['DELETE'])
def exit_act(user_id,activity_id):
	u1=user_id
	a1=activity_id
	user_id=User.getUser(user_id).id
	activity_id=Activity.getActivity(activity_id).id
	user_actif=Activity_user.query.filter_by(user_id=user_id, activity_id=activity_id,state=actif).first()
	if not(user_actif):
		return jsonify({"message":"user not found"})
	try:
		print('attend to actif')
		db.session.delete(user_actif)
		db.session.commit()
		user_attend=Activity_user.query.filter_by(activity_id=activity_id,state=attend).order_by(Activity_user.rank).first()
		new_user= Activity_user(user_id=user_attend.user_id, activity_id=activity_id, state=actif)
		db.session.delete(user_attend)
		db.session.add(new_user)
		# send_email_Activity('ent', User.query.filter_by(id=new_user.user_id).first().public_id, a1)
		# print('ent', User.query.filter_by(id=new_user.user_id).first().public_id, a1)
	except Exception as e:
		print('delete actif')
		db.session.delete(user_actif)
	print('ext', u1, a1)
	# send_email_Activity('ext', u1, a1)
	db.session.commit()
	return jsonify({"message":"seccus"})


@api.route('/all_act_pic',methods=['GET'])
def all_act_pic():
	def get(I):
		acts = [Activity_gallery.query.filter_by(id=i).first() for i in I]
		return [[act.id if i else 0 for i in [act.pic,act.vid] ] for act in acts]



	acts = [i for i in Activity_gallery.query.all()]
	acts.sort(key=lambda ac : ac.activity_id)
	glo = [([act.id for act in g],k) for k,g in groupby(acts,key=lambda x : x.activity_id)]
	print(glo)
	return jsonify([
		{'name':str(Activity.getActivitybyid(act_id).name),
		'items':get(i)
		} for i,act_id in glo])


def date(date,time):
	return datetime.datetime(year=date.year, month=date.month, day=date.day,hour=time.hour,minute=time.minute)
def str_min(min):
	print(str(min))
	if len(str(min))==1:
		return str(min)+'0' if min > 10 else '0'+str(min)
		
	return str(min)


@api.route('/actUsers/<activity_id>',methods=['GET'])
def actUsers(activity_id):
	act = Activity.query.filter_by(public_id=activity_id).first()
	act_id = act.id
	active_users = [User.query.filter_by(id=i.user_id).first() for i in Activity_user.query.filter_by(activity_id=act_id,state=actif).order_by(Activity_user.rank).all()]
	attend_users = [User.query.filter_by(id=i.user_id).first() for i in Activity_user.query.filter_by(activity_id=act_id,state=attend).order_by(Activity_user.rank).all()]
	return jsonify({
		"actif":{
			'length':str(len(active_users))+"/"+str(act.members),
			'data':[user.prenom+" "+user.nom for user in active_users]
		},
		"attend":{
			'length':str(len(attend_users)),
			'data':[user.prenom+" "+user.nom for user in attend_users]
		},
	})

@api.route('/all_act/',methods=['GET'])
def all_acts():
	current_time = datetime.datetime.utcnow()
	# for i in Activity.query.all():
	# 	print(date(i.date,i.heure))
	# 	print(current_time+datetime.timedelta(days=1))
	# 	print(date(i.date,i.heure)<current_time+datetime.timedelta(days=1))
	acts = [i for i in Activity.query.all() if date(i.date,i.heure) > current_time]
	# acts = Activity.query.all()
	print("het acts")
	acts.sort(key=lambda ac : ac.date)
	glo = [[ 
		{
			'public_id':str(act.public_id),
			'name':act.name,
			'date':conv(act.date),
			'time':str_min(act.heure.hour)+':'+str_min(act.heure.minute),
			'members':act.members,
			'submembers':act.getsubmembers(),
			'details':act.details,
			'city':act.city,
			'sep':act.sep,
			'state':actif if act.isActif() else attend,
			'submit':False,
			'can_submit':date(act.date,act.heure) > current_time+datetime.timedelta(days=1)
		}

	for act in g] for k,g in groupby(acts,key=lambda x : x.date)]
	return jsonify([{'date':str(i[0]['date']),'items':i} for i in glo])
 # 

@api.route('/all_act/<user_id>',methods=['GET'])
def all_act(user_id):
	current_time = datetime.datetime.utcnow()
	user=User.getUser(user_id)
	acts = [i for i in Activity.query.all() if date(i.date,i.heure) > current_time]
	acts.sort(key=lambda ac : ac.date)
	glo = [[ 
		{
			'public_id':str(act.public_id),
			'name':act.name,
			'date':conv(act.date),
			'time':str_min(act.heure.hour)+':'+str_min(act.heure.minute),
			'members':act.members,
			'submembers':act.getsubmembers(),
			'details':act.details,
			'city':act.city,
			'sep':act.sep,
			'state':act.getStatus(user.id),
			'submit':act.getSubmit(user.id),
			'can_submit':date(act.date,act.heure) > current_time+datetime.timedelta(days=1),
			'Ressep':not(act.sep and not(user.sep))

		}

	for act in g] for k,g in groupby(acts,key=lambda x : x.date)]
	return jsonify([{'date':str(i[0]['date']),'items':i} for i in glo])

@api.route('/my_act/',methods=['GET'])
def my_act0():
	return jsonify({
		"next":[],
		"prev":[]
		})
@api.route('/my_act/<user_id>',methods=['GET'])
def my_act(user_id):
	current_time = datetime.datetime.utcnow()
	user=User.getUser(user_id)
	return jsonify({
		"next":[
		{
			'public_id':str(act.public_id),
			'name':act.name,
			'date':conv(act.date),
			'time':str(act.heure.hour)+':'+str(act.heure.minute),
			'members':act.members,
			'submembers':act.getsubmembers1(user_id),
			'details':act.details,
			'city':act.city,
			'state':act.getStatus(user.id),
			'submit':act.getSubmit(user.id),
			'can_submit':date(act.date,act.heure) > current_time+datetime.timedelta(days = 1)
		}
		for act in user.getActivtyAvenir() if date(act.date,act.heure) > current_time+datetime.timedelta(days = 1) or act.getStatus(user.id)==actif ],
		"prev":[
		{
			'public_id':str(act.public_id),
			'name':act.name,
			'date':conv(act.date),
			'time':str(act.heure.hour)+':'+str(act.heure.minute),
			'members':act.members,
			'submembers':act.getsubmembers(),
			'details':act.details,
			'city':act.city,
			'state':act.getStatus(user.id),
			'submit':act.getSubmit(user.id)
		}
		for act in user.getActivtyPrecedent()]
		})


 

@api.route('/all_med',methods=['GET'])
def all_med():
	meds = Med.query.all()
	return jsonify([
		{
			'id' :i.id ,
			'nom' :i.nom ,
			'specialite' :i.specialite ,
			'ville' :i.ville ,
			'quartier' :i.quartier ,
			'tel' :i.tel ,
			'adresse' :i.adresse ,
			'email' :i.email 
		} 
		for i in meds])

# @api.route('/get_item/<name>',methods=['GET'])
# def get_item(name):
# 	id_=Item.query.filter_by(name=name).first().id
# 	# detail=Detail.query.filter_by(item_id=id_).first()
# 	return jsonify({
# 		'id':item.id,
# 		'details':item.details
# 		})
@api.route('/get_section/<name>',methods=['GET'])
def get_section(name):
	id_=Section.query.filter_by(name=name).first().id
	items=Item.query.filter_by(section_id=id_).order_by(Item.id).all()
	return jsonify([{
			'id':item.id,
			'name':item.name,
			'details':item.details,
			'vid':item.vid!=None,
			'pic':item.pic!=None
			} for item in items if not item.name in ['vid1','vid2']])

@api.route('/get_actualite',methods=['GET'])
def get_actualite():
	items=Actualite.query.all()
	return jsonify([{
			'id':item.id,
			'titre':item.titre,
			'details':item.details,
			'url':item.url,
			'vid':item.vid!=None,
			'pic':item.pic!=None
			} for item in items])

@api.route('/get_rubrique/<name>',methods=['GET'])
def get_rubrique(name):
	id_=Rubrique.query.filter_by(name=name).first().id
	return jsonify([{
		'value':i.value,
		'name':i.name
		} for i in Section.query.filter_by(rubrique_id=id_).all()])


 # *************************** Files handler *****************************

def handle(reader):
	data=[]
	header=[]
	def ind(k):
		if k in header:
			return header.index(k)
		return ['nom','specialite','ville','quartier','tel','adresse','email'].index(k)
	counter=0
	for i in reader:
		if counter==0:
			header=i
			print('header : ',header)
		else:
			row=i

			M=Med(
        nom =row[ind('nom')],
        specialite =row[ind('specialite')],
        ville =row[ind('ville')],
        quartier =row[ind('quartier')],
        tel =row[ind('tel')],
        adresse =row[ind('adresse')],
        email =row[ind('email')]
				)
			data.append(M)
		counter+=1
	return data



@api.route('/upload_csv', methods=['GET', 'POST'])
def upload():
	# try:
	if request.method == 'POST':
		file = request.files['file']
		if file and '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ['csv']:
			filename = secure_filename(file.filename)
			new_filename = f'{filename.split(".")[0]}_{str(datetime.datetime.now())[20:]}.csv'
			save_location = os.path.join('', new_filename)
			file.save(save_location)
			with open(save_location) as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=';')
				db.session.add_all(handle(csv_reader))
				db.session.commit()
	return redirect(url_for('sep_admin.data0',name='Med'))
	# except Exception as e:
		# return jsonify({'message':'make sure that you enter the data correctly the order is : \n Nom spécialité ville quartier adresse tel email'})









@api.route('/upload/<table>/<int:id>/<type_>', methods=['GET', 'POST'])
def index(table,id,type_):
	if request.method == 'POST':
		file = request.files['file']
		# if table=='Activity_gallery':
		ag=eval(f'{table}.getItem(id)')
		if type_=='img':
			ag.pic=file.read()
			ag.pic_name=file.filename
		else:
			ag.vid=file.read()
			ag.vid_name=file.filename
		db.session.commit()
		return f'Uploaded: {file.filename}'
	return jsonify({'message':'Post Reaquest Required'})
@api.route('/download/<table>/<int:id>/<type_>')
def download(table,id,type_):
	# upload = Upload.query.filter_by(id=upload_id).first()
	# if table=='Activity_gallery':
	ag=eval(f'{table}.getItem(id)')
	if type_=='img':
		return send_file(BytesIO(ag.pic), attachment_filename=ag.pic_name)
	return send_file(BytesIO(ag.vid), attachment_filename=ag.vid_name)

@api.route('/downloadCsv')
def downloadCsv():
	users = User.query.all()
	# header = ['name', 'area', 'country_code2', 'country_code3']
	# data = ['Afghanistan', 652090, 'AF', 'AFG']
	data=User.data_list(User.query.order_by(User.id).all())
	dd=[[str(i) for i in row[1:]] for row in data]

	test = lambda d: ''.join([i if i in [chr(32+i) for i in range(95)] else 'e' for i in d])
	csv='\n'.join([';'.join([test(j) for j in i]) for i in dd])

	return Response(
	csv,
	mimetype="text/csv",
	headers={"Content-disposition":
	"attachment; filename=myplot.csv"})
	# return send_file(BytesIO(f), attachment_filename='data.csv')

 # *************************** User handler *****************************

# @api.route('/checkEmail/<email>',methods=['GET'])# return true if email exist
# def checkEmail(email):
# 	users = User.query.all()
# 	user_ = [i for i in users if i.email.upper()==email.upper()]
# 	user = user_[0] if len(user_)>0 else []
# 	if user :
# 		return jsonify({'message':True})
# 	return jsonify({'message' : False})

@api.route('/getUser/<email>',methods=['GET'])
def getUserEmail(email):
	users = User.query.all()
	user_ = [i for i in users if i.email.upper()==email.upper()]
	user = user_[0] if len(user_)>0 else []
	if user :
		return jsonify({'message':False})
	try:
		isvalid=check_email(str(email),str(ProductionConfig.MAIL_CHECK_API_KEY))
		if(isvalid):
			return jsonify({'message' : True})
		else:
			return jsonify({'message':400 })
	except Exception as e:
		return jsonify({'message':e})
	return jsonify({'message' : True})

@api.route('/getToken_from_app',methods=['GET'])
def getToken_from_app():
	token = jwt.encode({'id' : 'test'}, ProductionConfig.SECRET_KEY, algorithm="HS256")
	return jsonify({'message':token})
# getToken_from_app

@api.route('/comfirmation',methods=['GET'])
def hello():
	user = User.query.first()
	return render_template("activatedAccount.html",user=user)

# 	return jsonify({"message":"hhhhhhhh"})
# @api.route('/activateUser/<user_id>',methods=['GET'])
# def getToken_from_app(user_id):
# 	token = jwt.encode({'id' : 'user_id'}, ProductionConfig.SECRET_KEY, algorithm="HS256")
# 	return jsonify({'message':token})

@api.route('/resetPassword/<email>/<recovery>',methods=['GET'])
def resetPassword(email,recovery):
	user = User.query.filter(func.lower(User.email) == func.lower(email)).first()
	if user:
		user = user if user.recovery==recovery else None
	if user :
		token = jwt.encode({'id' : str(user.public_id)}, ProductionConfig.SECRET_KEY, algorithm="HS256")
		return jsonify({'message':True,'token':token})
	return jsonify({'message':False})

@api.route('/setUser/<email>/<password>',methods=['GET'])
@token_required	
def changePassword(email,password):
	users = User.query.all()
	user_ = [i for i in users if i.email.upper()==email.upper()]
	user = user_[0] if len(user_)>0 else []
	if user :
		# user.password=generate_password_hash(password) #/////////////////////////// hash password //////////////////
		user.password=password #/////////////////////////// hash password //////////////////
		db.session.commit()
		return jsonify({'message':True})
	return jsonify({'message' : False})

@api.route('/getPassword/<email>',methods=['GET'])
def changePassword_(email):
	user = User.query.filter_by(email=email).first()
	if user :
		return jsonify({'message':user.password})
	return jsonify({'message' : False})
@api.route('/getUser/<email>/<password>',methods=['GET'])
def getUser(email,password):
	user = User.query.filter(func.lower(User.email) == func.lower(email)).first()
	if user:
		user = user if user.password==password else None
	else:
		return jsonify({'message' : 404})
	if user :
		token = jwt.encode({'id' : str(user.public_id)}, ProductionConfig.SECRET_KEY, algorithm="HS256")
		return jsonify({
			"public_id" :user.public_id,
			'nom' :user.nom,
			'prenom' :user.prenom,
			'date_naissance' :conv1(user.date_naissance),
			'ntel' :user.ntel,
			'debut_SEP' :user.debut_SEP,
			'sexe' :user.sexe,
			'metier' :user.metier,
			'loisirs' :user.loisirs,
			'ville_residence' :user.ville_residence,
			'grand_ville' :user.grand_ville,
			'medecin_traitant' :user.medecin_traitant,
			'traitement' :user.traitement,
			'couvMed' :user.couvMed,
			'email' :user.email,
			'password' :user.password,
			'auth' :user.auth,
			'sep' :user.sep,
			'active':user.active,
			'recovery':user.recovery,
			'token':token,

		})
	return jsonify({'message' : 'Token is invalid!'})
# grand_ville
@api.route('/getUsers',methods=['GET'])
def allUsers():
	users= User.query.filter_by(sep=True,active=True).all()
	def get(city):
		d=[i for i in data if i['name'].lower()==city.lower()]
		if d:
			return d[0]
		return {'lat':0,'long':0}
	def group(L):
		if len(L)>0:
			k = L[0].grand_ville
			users =[ i for i in L if i.grand_ville==k]
			myList=[{
				'city':k,
				'lat':get(k)['lat'],
				'long':get(k)['long'],
				'size':len(users),
				'users':[{
					'name':user.nom+' '+user.prenom,
					'ntel':user.ntel,
					'traitement':user.traitement,
					'medecin_traitant':user.medecin_traitant
					} 
				for user in users if user.auth==True]
			}]
			myList.extend(group([ i for i in L if i.grand_ville!=k]))
			return myList
		return []
	return jsonify([group(users),len(users)])


	# us=[([act for act in g],k) for k,g in groupby(users,key=lambda x : x.grand_ville)]
	# print(us)
	# out=[[
	# 		{
	# 		'city':k,
	# 		'lat':get(k)['lat'],
	# 		'long':get(k)['long'],
	# 		'size':len(list(g)),
			# 'users':[{
			# 	'name':i.nom+' '+i.prenom,
			# 	'ntel':i.ntel,
			# 	'traitement':i.traitement,
			# 	'medecin_traitant':i.medecin_traitant
			# 	} 
			# for i in list(g) if i.auth==True]
			# }
	# 	for g,k in us],len(users)]
	# # print(us)
	# return jsonify(out)
@api.route('/getCities',methods=['GET'])
def getCities():
	activites = Activity.query.all()
	acts_user = [i for i in activites if date(i.date,i.heure)<datetime.datetime.utcnow()-datetime.timedelta(days = 4)]
	print(acts_user)
	for act in acts_user:
		Activity_user.query.filter_by(activity_id=act.id).delete()
		# db.session.delete(act)
	db.session.commit()
	acts_gallery = [i for i in activites if date(i.date,i.heure)<datetime.datetime.utcnow()-datetime.timedelta(days = 360)]
	print(acts_gallery)
	for act in acts_gallery:
		Activity_gallery.query.filter_by(activity_id=act.id).delete()
		db.session.delete(act)
	db.session.commit()




	return jsonify([i['name'] for i in data])




@api.route('/activeUser',methods=['GET'])
def activeUser():
	try:
		token = request.values['token']
		if token==None:
			return jsonify({'message' : 'Token is missing!'}), 401
		try: 
			data = jwt.decode(token,ProductionConfig.SECRET_KEY, algorithms=["HS256"])
			user=User.query.filter_by(public_id=data['id']).first()
			user.active=True
			db.session.commit()
			return render_template("activatedAccount.html",user=user)
		except:
			return jsonify({'message' : 'Token is invalid!'}), 401

	except:
		return jsonify({'message':'An Error Occured'})




@api.route('/users/',methods=['POST'])
def users_post():
	data = request.get_json(force=True)
	u=User(
    nom =data['nom'],
    prenom =data['prenom'],
    date_naissance =conv_to_date(data['date_naissance']),
    ntel =data['ntel'],
    debut_SEP =data['debut_SEP'],
    sexe =data['sexe'],
    metier =data['metier'],
    loisirs =data['loisirs'],
    ville_residence =data['ville_residence'],
    grand_ville =data['grand_ville'],
    medecin_traitant =data['medecin_traitant'],
    traitement =data['traitement'],
    couvMed =data['couvMed'],
    email =data['email'],
    # password =generate_password_hash(data['password']),
    password =data['password'],
    auth =data['auth'],
    sep=data['sep'],
    viewed=False,
    active=False,
    recovery=generate()
	)
	db.session.add(u)
	db.session.commit()
	token=jwt.encode({'id' : str(u.public_id)}, ProductionConfig.SECRET_KEY, algorithm="HS256")
	url = request.base_url.split('/api')[0]+url_for('api.activeUser')+"?token="+token
	sended= send_email(u.email,url,u.recovery)
	if (not(sended)):
		db.session.delete(u)
		db.session.commit()
	return jsonify({'message':sended})


@api.route('/users/<user_id>',methods=['DELETE'])
@token_required
def users_delete(user_id):
	try:
		user=User.getUser(user_id)
		user_id1=user.id
		acts_actif = Activity_user.query.filter_by(user_id=user_id1,state=actif).all()
		for act in acts_actif:
			activity_public_id=Activity.query.filter_by(id=act.activity_id).first().public_id
			exit_act(user_id,activity_public_id)
			print(act)
		acts_attend = Activity_user.query.filter_by(user_id=user_id1,state=attend).all()
		for act in acts_attend:
			activity_public_id=Activity.query.filter_by(id=act.activity_id).first().public_id
			exit_att(user_id,activity_public_id)
		db.session.delete(user)
		db.session.commit()
		return jsonify({'message':True})
	except Exception as e:
		return jsonify({'message':False})
@api.route('/users/',methods=['PUT'])
@token_required
def users_put():
	try:
		data = request.get_json(force=True)
		user=User.getUser(data['public_id']) 
		u=User(
	    nom =data['nom'],
	    prenom =data['prenom'],
	    date_naissance =conv_to_date(data['date_naissance']),
	    ntel =data['ntel'],
	    debut_SEP =data['debut_SEP'],
	    sexe =data['sexe'],
	    metier =data['metier'],
	    loisirs =data['loisirs'],
	    ville_residence =data['ville_residence'],
	    grand_ville =data['grand_ville'],
	    medecin_traitant =data['medecin_traitant'],
	    traitement =data['traitement'],
	    couvMed =data['couvMed'],
	    email =data['email'],
	    password =data['password'],
	    # password =generate_password_hash(data['password']),
	    auth =data['auth'],
	    sep=data['sep']
			)
		user.setUser(u)
		db.session.commit()
		return jsonify({'message':True})
	except Exception as e:
		return jsonify({'message':False})


# abderafiechairi@gmail.com

@api.route('/mailing',methods=['POST'])
def mailingpost():
	data = request.get_json(force=True)
	# if (data['type']=='contact'):
	# 	send_contact(data['email'])
	# if (data['type']=='Réseau médical SEP'):
	# 	send_Res_med(data['email'])
	u=Mailing(
    date =datetime.datetime.now().date(),
    msg ='\n'.join([i+' : '+data[i] for i in data]),
    viewed=False
		)
	db.session.add(u)
	db.session.commit()
	return jsonify({'message':True})
	# /api/mailing/img

@api.route('/mailing/<id>',methods=['POST'])
def mailing_with_id(id):
	data = request.get_json(force=True)
	ag=Mailing.query.filter_by(id=id).first()
	ag.msg='\n'.join([i+' : '+data[i] for i in data])
	db.session.commit()
	return jsonify({'message':True})

@api.route('/mailing/img',methods=['POST'])
def mailingpostimg():
	file = request.files['file']
	if(str(file.filename).split('.')[-1]=='jpg'):
		ag=Mailing(
		date=datetime.datetime.now().date(),
		pic=file.read(),
		pic_name=file.filename,
		viewed=False
		)
	else:
		ag=Mailing(
		date=datetime.datetime.now().date(),
		vid=file.read(),
		vid_name=file.filename,
		viewed=False
		)		
	db.session.add(ag)
	db.session.commit()
	return jsonify({'id':ag.id})

@api.route('/vid/<name>',methods=['GET'])
def vid1(name):
	items=Item.query.filter_by(name=name).all()
	return jsonify([i.id for i in  items])



# Réseau médical SEP