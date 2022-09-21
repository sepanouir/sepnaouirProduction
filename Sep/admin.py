from .models import *
from flask import request,Blueprint,jsonify,send_file,redirect,render_template,url_for,session
import datetime	
from io import BytesIO
from itertools import groupby
from .forms import *
from sqlalchemy import desc
def conv(d):
	print(d)
	y,m,d=[int(i) for i in d.split('T')[0].split('-')]
	return datetime.date(y, m, d)
def convHome(o):
	T=['jan', 'fév', 'mars', 'avr', 'mai', 'juin', 'juil', 'août', 'sept', 'oct', 'nov', 'déc']
	return "{} {}".format(o.day, T[o.month-1])

admin=Blueprint('sep_admin','__name__',url_prefix='/sep_admin')


def replace_(s):
	ss=[i.split(' : ') for i in s.split('\n')]
	return ss 

# and request.endpoint != 'login'
# @admin.before_request
# def before_request():
#     if 'admin' not in session :
#         return redirect(url_for('api.login'))

@admin.route('/table/<url>/',methods=['GET'])
def tabls(url):
	url='/'.join(url.split('-'))
	return render_template('table.html',url='/'+url)


@admin.route('/home/',methods=['GET'])
def Home():
	users=User.query.filter_by(viewed=False).all()
	activity=Activity.query.order_by(desc(Activity.id)).first()
	mailings=Mailing.query.filter_by(viewed=False).all()
	mailings_msg=[replace_(i.msg) for i in mailings]
	# for i in range(len(mailings)):
	# 	mailings[i].msg=replace_(mailings[i].msg)
	# print([mail.img!=None for mail in mailings])
	out={}
	if activity:
		out={
			'activity':activity,
			'activity_actif':len(Activity_user.query.filter_by(activity_id=activity.id,state=actif).all()),
			'activity_attend':len(Activity_user.query.filter_by(activity_id=activity.id,state=attend).all()),
		}
	out['users']=users
	out['mailings']=mailings
	out['mailings_msg']=mailings_msg

	# out['mailing']=[]
	return render_template('home.html',data=out,conv=convHome,zip=zip)

@admin.route('/home/<table>/<int:id>',methods=['GET'])
def view(table,id):
	table=str.capitalize(table)
	item=eval(f'{table}.query.filter_by(id=id).first()')
	item.viewed=True
	db.session.commit()
	return redirect(url_for('sep_admin.Home'))

@admin.route('/ActivityUsers/<int:activity_id>',methods=['GET'])
def ActivityUsers(activity_id):
	act = Activity.query.filter_by(id=activity_id).first()
	users=[User.query.filter_by(id=u.user_id).first() for u in Activity_user.query.filter_by(activity_id=activity_id,state=actif)]
	data=[[user.prenom+" "+user.nom,user.grand_ville,user.email]
		for user in users]
	# data.sort(keys=lambda x : x[1])
	header=['Nom','Ville','email']
	return render_template('ActivityUser.html',header=header,data=data,act_name=act.name)


@admin.route('/data/<string:name>',methods=['GET'])
def data0(name):
	final_name={
	'User':'utilisateurs',
	'Activity':'Activités',
	'Med':'Réseau des médecines'
	}
	name=str.capitalize(name)
	table = eval(f'{name}.data_list({name}.query.order_by({name}.id).all())')
	head=table.pop(0)
	if name=='Activity':
		table=[
			[
				len(Activity_user.query.filter_by(activity_id=act.id,state=actif).all()),
				act.id,
				act.name,
				act.date,
				act.heure,
				act.members,
				act.details,
				act.city,
				act.sep

			]
			for act in Activity.query.order_by(Activity.id).all()]
		return render_template('dataActivity.html',data=table,name=name,update=lambda x:x[2:])
	if name=='Item':
		return redirect(url_for('sep_admin.Home'))
	if name=='Activity_gallery':
		return render_template('dataGallery.html',head=head,data=table,name=name)
	if name=='Actualite':
		return render_template('dataActualite.html',head=head,data=table,name=name)
	if name=='Mailing':
		replace={'pic':'image','vid':'video'}
		head=[replace[i] if i in replace.keys() else i for i in head]
		print(table)
		for i in range(0,len(table)):
			table[i][2]=replace_(table[i][2])
			print(table[i][2])
		return render_template('dataMailing.html',head=head[1:-1],data=table,name=name)
	return render_template('data.html',head=head,data=table,name=name,final_name=final_name[name],update=lambda x:x[1:])

@admin.route('/data-section/<string:name>',methods=['GET'])
def data1(name):
	name=str.capitalize(name)
	print(name)
	section=Section.getSection(name)
	id_=section.id
	table = Item.data_list(Item.query.filter_by(section_id=id_).order_by(Item.id).all())
	head=table.pop(0)
	replace={'pic':'image','vid':'video'}
	head=[replace[i] if i in replace.keys() else i for i in head]
	print(head)
	return render_template('dataSection.html',head=head[1:],data=table,name=name,final_name=section.value)

@admin.route('/edit/<table>/<int:id>', methods=['GET','POST'])
def edit(table,id=0):
	d="sep_admin.data0"
	t=table
	if not table in forms.keys() or table=='Item':
		table = 'Item' 
		d='sep_admin.data1'
		t=Section.query.filter_by(id=Item.query.filter_by(id=id).first().section_id).first().name
	if request.method=='POST':
		print('post request §§§§§§')
		form = forms[table]()
		form.set(type_='edit',id=id)
		# if form.validate_on_submit():
			# print('form validate on submit')
		return redirect(url_for(d,name=t))
	item=eval(f'{table}.query.filter_by(id=id).first()')
	form = forms[table](obj=item)
	return render_template('edit.html', form=form,id=id,name=table,redirect=url_for(d,name=t))

@admin.route('/delete/<table>/<int:id>/<media>')
def deleteVid(table,id,media):
	item = eval(f'{table}.query.filter_by(id=id).first()')
	if media == 'vid':
		item.vid=None
		item.vid_name=None
	if media == 'pic':
		item.pic=None
		item.pic_name=None	
	db.session.commit()
	if table == 'Activity':
		return redirect('/sep_admin/data/'+table)
	if table == 'User':
		return redirect('/sep_admin/data/'+table)
	if table in forms.keys() and table!='Item':
		return redirect('/sep_admin/data/'+table)
	else:
		item=Item.query.filter_by(id=id).first()
		section_name=Section.query.filter_by(id=item.section_id).first().name
		return redirect('/sep_admin/data-section/'+section_name)

@admin.route('/delete/<table>/<int:id>')
def delete(table,id):
	if table == 'Activity':
		for i in Activity_user.query.filter_by(activity_id=id).all():
			db.session.delete(i)
		for i in Activity_gallery.query.filter_by(activity_id=id).all():
			db.session.delete(i)
		db.session.delete(Activity.query.filter_by(id=id).first())
		db.session.commit()
		return redirect('/sep_admin/data/'+table)
	if table == 'User':
		for i in Activity_user.query.filter_by(user_id=id).all():
			db.session.delete(i)
		db.session.delete(User.query.filter_by(id=id).first())
		db.session.commit()
		return redirect('/sep_admin/data/'+table)
	if table in forms.keys() and table!='Item':
		item=eval(f'{table}.query.filter_by(id=id).first()')
		db.session.delete(item)
		db.session.commit()
		return redirect('/sep_admin/data/'+table)
	else:
		item=Item.query.filter_by(id=id).first()
		section_name=Section.query.filter_by(id=item.section_id).first().name
		db.session.delete(item)
		db.session.commit()
		return redirect('/sep_admin/data-section/'+section_name)

@admin.route('/add/<table>/',methods=['GET','POST'])
def add(table):
	form = forms[table]()
	if request.method=='POST':	
		form.set(type_='add')
		return redirect('/sep_admin/data/'+table)
	return render_template('add.html',form=form,table=table,redirect='/sep_admin/data/'+table)

@admin.route('/add-section/<section>/',methods=['GET','POST'])
def addSection(section):
	id_=Section.getSection(section).id
	form = forms['Item']()
	if request.method=='POST':	
		form.add(section_id=id_)
		return redirect('/sep_admin/data-section/'+section)
	return render_template('add.html',form=form,table='Item',section=section,redirect='/sep_admin/data-section/'+section)

@admin.route('/clean',methods=['GET'])
def clean():
	a=Activity_user.query.all()
	for i in a:
		print(i)
		db.session.delete(i)
	db.session.commit()
	return jsonify({'message':True})






# # ******************* Users ******************

# @admin.route('/users/',methods=['GET'])
# def users_get():
# 	return User.users_get()

# @admin.route('/users/<id_>',methods=['PUT'])
# def users_put(id_):
# 	data = request.get_json(force=True)
# 	u=User(
#     public_id =id_,
#     nom =data['nom'],
#     prenom =data['prenom'],
#     date_naissance =data['date_naissance'],
#     debut_SEP =data['debut_SEP'],
#     sexe =data['sexe'],
#     metier =data['metier'],
#     loisirs =data['loisirs'],
#     ville_residence =data['ville_residence'],
#     medecin_traitant =data['medecin_traitant'],
#     couvMed =data['couvMed'],
#     email =data['email'],
#     password =data['password'],
#     auth =data['auth'],
#     sep=data['sep']
# 		)
# 	return User.users_put(u)




# @admin.route('/users/<id_>',methods=['DELETE'])
# def users_delete(id_):
# 	return User.user_delete(id_)

# # ******************* Meds ******************

# @admin.route('/meds/',methods=['GET'])
# def meds_get():
# 	return Med.meds_get()

# @admin.route('/meds/<id_>',methods=['PUT'])
# def meds_put(id_):
# 	data = request.get_json(force=True)
# 	m=Med(
# 		id = data['id']
#         ,nom = data['nom']
#         ,specialite = data['specialite']
#         ,ville = data['ville']
#         ,quartier = data['quartier']
#         ,tel = data['tel']
#         ,adresse = data['adresse']
#         ,email = data['email']
# 		)
# 	return Med.meds_put(m)


# @admin.route('/meds/',methods=['POST'])
# def meds_post():
# 	data = request.get_json(force=True)
# 	m=Med(
#         nom = data['nom']
#         ,specialite = data['specialite']
#         ,ville = data['ville']
#         ,quartier = data['quartier']
#         ,tel = data['tel']
#         ,adresse = data['adresse']
#         ,email = data['email']
# 		)
# 	return Med.meds_post(m)

# @admin.route('/meds/<id_>',methods=['DELETE'])
# def meds_delete(id_):
# 	return Med.meds_delete(id_)

# # ******************* Activities ******************

# @admin.route('/activities/',methods=['GET'])
# def activities_get():
# 	return Activity.activities_get()

# @admin.route('/activities/<id_>',methods=['PUT'])
# def activities_put(id_):
# 	data = request.get_json(force=True)
# 	return Activity.activities_put(Activity(public_id=id_,name=data['name'],date=conv(data['date']),members=data['members'],details=data['details'],city=data['city']))


# @admin.route('/activities/',methods=['POST'])
# def activities_post():
# 	data = request.get_json(force=True)
# 	return Activity.activities_post(Activity(name=data['name'],date=conv(data['date']),members=data['members'],details=data['details'],city=data['city']))

# @admin.route('/activities/<id_>',methods=['DELETE'])
# def activities_delete(id_):
# 	return Activity.activities_delete(id_)

# # ******************* Items ******************

# @admin.route('/sections/<name>/',methods=['GET'])
# def sections_get(name):
# 	id_ =Section.getSection(name).id
# 	return Item.items_get(id_,name)

# @admin.route('/sections/<name>/<id_>',methods=['PUT'])
# def sections_put(name,id_):
# 	data = request.get_json(force=True)
# 	return Item.items_put(id=id_,name=data['name'],details=data['details'])


# @admin.route('/sections/<name>/',methods=['POST'])
# def setcions_post(name):
# 	data = request.get_json(force=True)
# 	id_ =Section.getSection(name).id
# 	if 'details' in data:
# 		return Item.items_post(Item(section_id=id_,name=data['name'],details=data['details']))
# 	return Item.items_post(Item(section_id=id_,name=data['name']))
