from sqlalchemy_utils import UUIDType
from flask_sqlalchemy import SQLAlchemy
from .serialize import Serializer
from flask import jsonify
from sqlalchemy import desc
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
attend='attend'
actif='actif'
db=SQLAlchemy()

def date(date,time):
    return datetime.datetime(year=date.year, month=date.month, day=date.day,hour=time.hour,minute=time.minute)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.Text,nullable=False)


class User(db.Model,Serializer):
    excluded_columns=['public_id','Activity_user','password','viewed']

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id = db.Column(UUIDType(binary=False),default=uuid.uuid1,unique=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    date_naissance = db.Column(db.Date)
    debut_SEP = db.Column(db.String(50))
    ntel = db.Column(db.String(50))
    sexe = db.Column(db.String(50))
    metier = db.Column(db.String(50))
    loisirs = db.Column(db.String(50))
    ville_residence = db.Column(db.String(50))
    grand_ville = db.Column(db.String(50))
    medecin_traitant = db.Column(db.String(50))
    traitement = db.Column(db.String(50))
    couvMed = db.Column(db.String(50))
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.Text,nullable=False)
    auth = db.Column(db.Boolean)
    sep= db.Column(db.Boolean)
    viewed= db.Column(db.Boolean)
    active= db.Column(db.Boolean)
    recovery= db.Column(db.String(50))
    def __repr__(self):
        return 'Utilisateur %r' % self.email


    def setUser(self,user):
        print(user.date_naissance)
        self.nom =user.nom 
        self.prenom =user.prenom 
        self.date_naissance =user.date_naissance 
        self.debut_SEP =user.debut_SEP 
        self.ntel =user.ntel 
        self.sexe =user.sexe 
        self.metier =user.metier 
        self.loisirs =user.loisirs 
        self.ville_residence =user.ville_residence 
        self.grand_ville =user.grand_ville 
        self.medecin_traitant =user.medecin_traitant 
        self.traitement =user.traitement 
        self.couvMed =user.couvMed 
        self.email =user.email 
        self.password =user.password 
        self.auth =user.auth 
        self.sep= user.sep
        self.viewed= user.viewed



    @staticmethod
    def getUser(public_id):
        return User.query.filter_by(public_id=public_id).first()

    @staticmethod
    def checkUser(email,password):
        user=User.query.filter_by(email=email).first()
        if user:
            # if check_password_hash(user.password,password):
            if user.password==password:
                return user
        return None

    def getActivtyAvenir(self):
        current_time = datetime.datetime.utcnow()
        acts_users = Activity_user.query.filter_by(user_id=self.id).all()
        acts = [Activity.getActivitybyid(act.activity_id) for act in acts_users ]#if act.date >current_time]
        return [act for act in acts if date(act.date,act.heure) > current_time-datetime.timedelta(days=1)]

    def getActivtyPrecedent(self):
        current_time = datetime.datetime.utcnow()
        acts_users = Activity_user.query.filter_by(user_id=self.id,state=actif).all()
        acts = [Activity.getActivitybyid(act.activity_id) for act in acts_users ]#if date(act.date,act.heure) >current_time]
        return [act for act in acts if date(act.date,act.heure) <= current_time-datetime.timedelta(days=1)]


class Activity(db.Model,Serializer):
    excluded_columns=['public_id','Activity_user','Activity_Gallery','activity']

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    public_id = db.Column(UUIDType(binary=False),default=uuid.uuid1,unique=True)
    name = db.Column(db.String(50))
    date = db.Column(db.Date)
    heure = db.Column(db.Time)
    members = db.Column(db.Integer)
    details = db.Column(db.Text)
    city = db.Column(db.String(20))
    sep= db.Column(db.Boolean)

    def setActivity(self,newAct):
        self.name=newAct.name
        self.date=newAct.date
        self.heure=newAct.heure
        self.members=newAct.members
        self.details=newAct.details
        self.city=newAct.city
        self.sep=newAct.sep

    def __repr__(self):
        return str(self.name)
    @staticmethod
    def getActivity(public_id):
        return Activity.query.filter_by(public_id=public_id).first()
    @staticmethod
    def getActivitybyid(id_):
        return Activity.query.filter_by(id=id_).first()
    # @staticmethod
    def getActif(self):
        return len(Activity_user.query.filter_by(activity_id=self.id,state=actif).all())
    
    def getAttend(self):
        return len(Activity_user.query.filter_by(activity_id=self.id,state=attend).all())
    def isActif(self):
        return len(Activity_user.query.filter_by(activity_id=self.id,state=actif).all())<self.members
    def getsubmembers(self):
        # if self.getActif()==self.members:
        #     if self.getAttend() > 0 :
        #         return self.getAttend()
        return self.getActif()

    def getsubmembers1(self,user_id):
        if self.getActif()==self.members:
            if self.getAttend() > 0 :
                acts = [i.user_id for i in Activity_user.query.filter_by(activity_id=self.id,state=attend).all()]
                print(acts)
                user_id = User.getUser(user_id).id
                return acts.index(user_id)+1
        return self.getActif()

    def getSubmit(self,user_id):
        return len(Activity_user.query.filter_by(user_id=user_id,activity_id=self.id).all())==1
    def getStatus(self,user_id):
        act =Activity_user.query.filter_by(user_id=user_id,activity_id=self.id).first()
        if act :
            return act.state
        return actif
    @staticmethod
    def getActsbyUser(public_id):
        id_=User.getUser(public_id).id
        acts_id=Activity_user.query.filter_by(user_id=id_).all()
        return [Activity.query.filter_by(id=act.activity_id).first() for act in acts_id]


class Activity_user(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'),nullable=False)
    user = db.relationship('User', backref=db.backref('Activity_user', lazy='dynamic'))
    activity = db.relationship('Activity', backref=db.backref('Activity_user', lazy='dynamic'))
    state = db.Column(db.Text)
    rank = db.Column(db.Integer,nullable=False)

    def __init__(self,user_id,activity_id,state):
        super(Activity_user, self).__init__()
        self.user_id=user_id
        self.activity_id=activity_id
        self.state=state
        A=Activity_user.query.filter_by(activity_id=self.activity_id,state=self.state).order_by(desc(Activity_user.rank)).all()
        if A : 
            print('max rank',A[0].rank)
            self.rank=A[0].rank+1
        else:
            self.rank=1


    def len_activity(self):
        l=Activity_user.query.filter_by(activity_id=self.activity_id,state=self.state).all()
        return len(l)

    def getRank(self):
        rank=self.rank-Activity_user.query.filter_by(activity_id=self.activity_id,state=self.state)\
                            .order_by(desc(Activity_user.rank)).first().rank
        return rank


class Rubrique(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    def __repr__(self):
        return 'Rubrique %r' % self.name

    @staticmethod
    def getId(value):
        return Rubrique.query.filter_by(name=value).first().id


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    value = db.Column(db.String(50))
    name = db.Column(db.String(50))
    rubrique_id = db.Column(db.Integer, db.ForeignKey('rubrique.id'))
    rubrique = db.relationship('Rubrique', backref=db.backref('Section', lazy='dynamic'))
    def __repr__(self):
        return 'Section %r' % self.name
    @staticmethod
    def getSection(name):
        return Section.query.filter_by(name=name).first()


class Item(db.Model,Serializer):
    excluded_columns=['pic_name','vid_name','section_id','section']
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    details = db.Column(db.Text)
    pic = db.Column(db.LargeBinary)
    pic_name = db.Column(db.String(50))
    vid = db.Column(db.LargeBinary)
    vid_name = db.Column(db.String(50))
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    section = db.relationship('Section', backref=db.backref('Item', lazy='dynamic'))
    def __repr__(self):
        return 'Item %r' % self.name

    def setItem(self,newItem):
        self.name =newItem.name
        self.details =newItem.details
        self.pic =newItem.pic
        self.pic_name =newItem.pic_name
        self.vid =newItem.vid
        self.vid_name =newItem.vid_name
        self.section_id =newItem.section_id

    @staticmethod
    def getItem(_id):
        return Item.query.filter_by(id=_id).first()

class Med(db.Model,Serializer):

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nom = db.Column(db.String(50))
    specialite = db.Column(db.String(50))
    ville = db.Column(db.String(20))
    quartier = db.Column(db.String(50))
    tel = db.Column(db.String(15))
    adresse = db.Column(db.String(50))
    email = db.Column(db.String(50),nullable=False,unique=True)
    
    def setmed(self,med):
        self.nom = med.nom
        self.specialite = med.specialite
        self.ville = med.ville
        self.quartier = med.quartier
        self.tel = med.tel
        self.adresse = med.adresse
        self.email = med.email
        
        


    def __repr__(self):
        return 'Med %r' % self.nom

    def meds_delete(id_):
        med = Med.query.filter_by(id=id_).first()
        db.session.delete(med)
        db.session.commit()
        return jsonify({'message':'done'})



class Activity_gallery(db.Model,Serializer):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    pic = db.Column(db.LargeBinary)
    pic_name = db.Column(db.String(50))
    vid = db.Column(db.LargeBinary)
    vid_name = db.Column(db.String(50))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    activity = db.relationship('Activity', backref=db.backref('Activity_Gallery', lazy='dynamic'))

    @staticmethod
    def getItem(id_):
        return Activity_gallery.query.filter_by(id=id_).first()


    def setItem(self,newItem):
        print('on set activity gallery item')
        self.pic =newItem.pic
        self.pic_name =newItem.pic_name
        self.vid =newItem.vid
        self.vid_name =newItem.vid_name
        self.activity_id =newItem.activity_id

class Actualite(db.Model,Serializer):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    titre = db.Column(db.String(50))
    details = db.Column(db.Text)
    url = db.Column(db.Text)
    pic = db.Column(db.LargeBinary)
    pic_name = db.Column(db.String(50))
    vid = db.Column(db.LargeBinary)
    vid_name = db.Column(db.String(50))

    @staticmethod
    def getItem(id_):
        return Actualite.query.filter_by(id=id_).first()


    def setItem(self,newItem):
        self.titre =newItem.titre
        self.details =newItem.details
        self.url =newItem.url
        self.pic =newItem.pic
        self.pic_name =newItem.pic_name
        self.vid =newItem.vid
        self.vid_name =newItem.vid_name


class Mailing(db.Model,Serializer):
    excluded_columns=['pic_name','vid_name']

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    date = db.Column(db.Date)
    msg = db.Column(db.Text)
    pic = db.Column(db.LargeBinary)
    pic_name = db.Column(db.String(50))
    vid = db.Column(db.LargeBinary)
    vid_name = db.Column(db.String(50))
    viewed= db.Column(db.Boolean)
    @staticmethod
    def getItem(id_):
        return Mailing.query.filter_by(id=id_).first()

    @staticmethod
    def get(email):
        A=Mailing.query.filter_by(pic_name=email).order_by(desc(Mailing.pic_name)).first()
        return A

    def setItem(self,newItem):
        self.msg=newItem.msg
        self.date=newItem.date
        self.pic =newItem.pic
        self.pic_name =newItem.pic_name
        self.vid =newItem.vid
        self.vid_name =newItem.vid_name
        self.viewed=False
