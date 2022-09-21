from wtforms import StringField, PasswordField,DateField,FileField,IntegerField,BooleanField,TextAreaField,TimeField
from wtforms.validators import InputRequired, Length, AnyOf,Email,EqualTo
from flask_wtf import FlaskForm 
from .models import *
from flask import request
from wtforms_sqlalchemy.fields import QuerySelectField
import email_validator

class Login(FlaskForm):
    email = StringField('Email', validators=[InputRequired('champ requis'),Email("Email invalid")])
    password = StringField('mot de passe', validators=[InputRequired('champ requis'),Length(min=8,message='Votre mot de passe doit comporter 8 caractères (chiffres, lettres et caractères spéciaux)')])

    def isEmpty(self):
        if(Admin.query.all()):
            return False
        return True

    def isValid(self):
        amin = Admin.query.first()
        return  amin.email==self.email.data and amin.password == self.password.data

class Register(FlaskForm):
    email = StringField('Email', validators=[InputRequired('champ requis'),Email("Email invalid")])
    password = StringField('mot de passe', validators=[InputRequired('champ requis'),Length(min=8,message='Votre mot de passe doit comporter 8 caractères (chiffres, lettres et caractères spéciaux)')])
class Update(FlaskForm):
    email = StringField('Email', validators=[InputRequired('champ requis'),Email("Email invalid")])
    password = StringField('mot de passe', validators=[InputRequired('champ requis'),Length(min=8,message='Votre mot de passe doit comporter 8 caractères (chiffres, lettres et caractères spéciaux)')])
    confPassword = StringField('Confirmez le mot de passe', validators=[InputRequired('champ requis'),EqualTo('password', message='Mot de passe incompatible')])




# grand_ville
class UserForm(FlaskForm):
    nom = StringField('Nom', validators=[InputRequired()])
    prenom = StringField('Prénom', validators=[InputRequired()])
    date_naissance = DateField('Date de naissance', validators=[InputRequired()])
    debut_SEP = StringField('Début de Sep', validators=[InputRequired()])
    ntel = StringField('Numéro de téléphone', validators=[InputRequired()])
    sexe = StringField('Sexe', validators=[InputRequired()])
    metier = StringField('Métier', validators=[InputRequired()])
    loisirs = StringField('Loisirs', validators=[InputRequired()])
    ville_residence = StringField('Ville residence', validators=[InputRequired()])
    grand_ville = StringField('Ville mitoyenne', validators=[InputRequired()])
    medecin_traitant = StringField('Médecin traitant', validators=[InputRequired()])
    traitement = StringField('traitement', validators=[InputRequired()])
    couvMed = StringField('Couverture médicale', validators=[InputRequired()])
    # password = StringField('mot de passe', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    auth = BooleanField()
    sep = BooleanField()
    # viewed = BooleanField()

    def set(self,type_,id=0):

        if type_=='edit':
            user = User.query.filter_by(id=id).first()
            newUser=User(
            nom = self.nom.data,
            prenom = self.prenom.data,
            date_naissance = self.date_naissance.data,
            debut_SEP = self.debut_SEP.data,
            ntel = self.ntel.data,
            sexe = self.sexe.data,
            metier = self.metier.data,
            loisirs = self.loisirs.data,
            ville_residence = self.ville_residence.data,
            grand_ville = self.grand_ville.data,
            medecin_traitant = self.medecin_traitant.data,
            traitement = self.traitement.data,
            couvMed = self.couvMed.data,
            email = self.email.data,
            auth = self.auth.data,
            password=user.password,
            sep = self.sep.data,
            viewed = False
        )
            user.setUser(newUser)
        elif type_=='add':
            newUser=User(
            nom = self.nom.data,
            prenom = self.prenom.data,
            date_naissance = self.date_naissance.data,
            debut_SEP = self.debut_SEP.data,
            ntel = self.ntel.data,
            sexe = self.sexe.data,
            metier = self.metier.data,
            loisirs = self.loisirs.data,
            ville_residence = self.ville_residence.data,
            grand_ville = self.grand_ville.data,
            medecin_traitant = self.medecin_traitant.data,
            traitement = self.traitement.data,
            couvMed = self.couvMed.data,
            email = self.email.data,
            auth = self.auth.data,
            password='12345678',
            sep = self.sep.data,
            viewed = False
        )  
            db.session.add(newUser)
        db.session.commit()
        return True



class ActivityForm(FlaskForm):
    name = StringField('Nom', validators=[InputRequired()])
    date = DateField('Date',validators=[InputRequired()])
    heure = TimeField('Heure',validators=[InputRequired()])
    members = IntegerField('membres',validators=[InputRequired()])
    details = TextAreaField('détails',validators=[InputRequired()])
    city = StringField('ville', validators=[InputRequired()])
    sep =  BooleanField()

    def set(self,type_,id=0):
        new = Activity(
            name = self.name.data,
            date = self.date.data,
            heure = self.heure.data,
            members = self.members.data,
            details = self.details.data,
            city = self.city.data,
            sep = self.sep.data
            )
        if type_=='edit':
            prev = Activity.query.filter_by(id=id).first()
            prev.setActivity(new)
        elif type_=='add':
            db.session.add(new)
        db.session.commit()
        return True

class MedForm(FlaskForm):
    nom = StringField('Nom et prénom', validators=[InputRequired()])
    specialite = StringField('Spécialité', validators=[InputRequired()])
    ville = StringField('ville', validators=[InputRequired()])
    quartier = StringField('Quartier', validators=[InputRequired()])
    tel = StringField('N° tel', validators=[InputRequired()])
    adresse = StringField('Adresse', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

    def set(self,type_,id=0):
        new = Med(
            nom = self.nom.data,
            specialite = self.specialite.data,
            ville = self.ville.data,
            quartier = self.quartier.data,
            tel = self.tel.data,
            adresse = self.adresse.data,
            email = self.email.data
            )
        if type_=='edit':
            prev = Med.query.filter_by(id=id).first()
            prev.setmed(new)
        elif type_=='add':
            db.session.add(new)
        db.session.commit()
        return True   

class MailingForm(FlaskForm):
    date = DateField('date', validators=[InputRequired()])
    msg = TextAreaField('message', validators=[InputRequired()])
    pic=FileField('photo')
    vid=FileField('video')

    def set(self,type_,id=0):
        pic,vid=None,None
        if self.pic.data:
            pic = request.files[self.pic.name]
        if self.vid.data:
            vid = request.files[self.vid.name]
        if type_=='edit':
            prev = Mailing.query.filter_by(id=id).first()
            new = Mailing(
                date=self.date.data,
                msg=self.msg.data,
                pic = pic.read() if self.pic.data else prev.pic,
                pic_name = pic.filename if self.pic.data else prev.pic_name,
                vid = vid.read() if self.vid.data else prev.vid,
                vid_name = vid.filename if self.vid.data else prev.vid_name,
                )

            prev.setItem(new)
        elif type_=='add':
            new = Mailing(
                date=self.date.data,
                msg=self.msg.data,
                pic = pic.read() if self.pic.data else None,
                pic_name = pic.filename if self.pic.data else None,
                vid = vid.read() if self.vid.data else None,
                vid_name = vid.filename if self.vid.data else None,
                viewed=False
                )
            db.session.add(new)
        db.session.commit()
        return True  


class ItemForm(FlaskForm):
    name=StringField('nom',validators=[InputRequired()])
    details=TextAreaField('details')
    pic=FileField('photo')
    vid=FileField('video')

    def set(self,type_,id=0):
        section_id=Item.getItem(id).section_id
        pic,vid=None,None
        if self.pic.data:
            pic = request.files[self.pic.name]
        if self.vid.data:
            vid = request.files[self.vid.name]
        prev = Item.getItem(id)
        new = Item(
            name = self.name.data,
            details = self.details.data,
            pic = pic.read() if self.pic.data else prev.pic,
            pic_name = pic.filename if self.pic.data else prev.pic_name,
            vid = vid.read() if self.vid.data else prev.vid,
            vid_name = vid.filename if self.vid.data else prev.vid_name,
            section_id = section_id
            )
        prev.setItem(new)
        db.session.commit()
        return True   
    def add(self,section_id=0):

        pic,vid=None,None
        if self.pic.data:
            pic = request.files[self.pic.name]
        if self.vid.data:
            vid = request.files[self.vid.name]
        new = Item(
            name = self.name.data,
            details = self.details.data,
            pic = pic.read() if self.pic.data else None,
            pic_name = pic.filename if self.pic.data else None,
            vid = vid.read() if self.vid.data else None,
            vid_name = vid.filename if self.vid.data else None,
            section_id = section_id
            )
        db.session.add(new)
        db.session.commit()
        return True   





def query_select():
    return Activity.query


class GalleryForm(FlaskForm):
    activity = QuerySelectField('activity',query_factory=query_select,get_label='name')  
    pic=FileField('photo')
    vid=FileField('video')

    def set(self,type_,id=0):
        activity_id=Activity.query.filter_by(name=str(self.activity.data)).first().id
        pic,vid=None,None
        if self.pic.data:
            pic = request.files[self.pic.name]
        if self.vid.data:
            vid = request.files[self.vid.name]
        # new = Activity_gallery(
        #     pic = pic.read() if self.pic.data else None,
        #     pic_name = pic.filename if self.pic.data else None,
        #     vid = vid.read() if self.vid.data else None,
        #     vid_name = vid.filename if self.vid.data else None,
        #     activity_id = activity_id
        #     )
        # if type_=='add':
        #     db.session.add(new)
        # else:
        #     print("set gallery item")
        #     print('self.pic.data : ',bool(self.pic.data))
        #     print('self.vid.data : ',bool(self.vid.data))
        #     prev = Activity_gallery.getItem(id)
        #     new = Activity_gallery(
        #     pic = pic.read() if self.pic.data else prev.pic,
        #     pic_name = pic.filename if self.pic.data else prev.pic_name,
        #     vid = vid.read() if self.vid.data else prev.vid,
        #     vid_name = vid.filename if self.vid.data else prev.vid_name,
        #     activity_id = activity_id
        #     )
        #     prev.setItem(new)
        if type_=='edit':
            prev = Activity_gallery.getItem(id)
            new = Activity_gallery(
                activity_id = activity_id,
                pic = pic.read() if self.pic.data else prev.pic,
                pic_name = pic.filename if self.pic.data else prev.pic_name,
                vid = vid.read() if self.vid.data else prev.vid,
                vid_name = vid.filename if self.vid.data else prev.vid_name,
                )

            prev.setItem(new)
        elif type_=='add':
            new = Activity_gallery(
                activity_id = activity_id,
                pic = pic.read() if self.pic.data else None,
                pic_name = pic.filename if self.pic.data else None,
                vid = vid.read() if self.vid.data else None,
                vid_name = vid.filename if self.vid.data else None,
                )
            db.session.add(new)


        db.session.commit()
        return True   
class ActualiteForm(FlaskForm):
    titre=StringField('titre',validators=[InputRequired()])
    details=TextAreaField('details',validators=[InputRequired()])
    url=StringField('url')
    pic=FileField('photo')
    vid=FileField('video')

    def set(self,type_,id=0):
        pic,vid=None,None
        if self.pic.data:
            pic = request.files[self.pic.name]
        if self.vid.data:
            vid = request.files[self.vid.name]

        if type_=='add':
            new = Actualite(
                titre=self.titre.data,
                details=self.details.data,
                url=self.url.data,
                pic = pic.read() if self.pic.data else None,
                pic_name = pic.filename if self.pic.data else None,
                vid = vid.read() if self.vid.data else None,
                vid_name = vid.filename if self.vid.data else None,
                )
            db.session.add(new)
        else:
            print('edir actualité')
            print(bool(self.pic.data))
            print(bool(self.vid.data))
            prev = Actualite.getItem(id)
            new = Actualite(
                titre=self.titre.data,
                details=self.details.data,
                url=self.url.data,
                pic = pic.read() if self.pic.data else prev.pic,
                pic_name = pic.filename if self.pic.data else prev.pic_name,
                vid = vid.read() if self.vid.data else prev.vid,
                vid_name = vid.filename if self.vid.data else prev.vid_name,
                )
            prev.setItem(new)
        db.session.commit()
        return True   
    # def add(self,section_id=0):
    #     activity_id=Activity.query.filter_by(name=activity.).id
    #     pic,vid=None,None
    #     if self.pic.data:
    #         pic = request.files[self.pic.name]
    #     if self.vid.data:
    #         vid = request.files[self.vid.name]
    #     new = Activity_gallery(
    #         pic = pic.read() if self.pic.data else None,
    #         pic_name = pic.filename if self.pic.data else None,
    #         vid = vid.read() if self.vid.data else None,
    #         vid_name = vid.filename if self.vid.data else None,
    #         activity_id = activity_id
    #         )
    #     db.session.add(new)
    #     db.session.commit()
    #     return True   














forms={
    'User':UserForm,
    'Activity':ActivityForm,
    'Med':MedForm,
    'Item':ItemForm,
    'Activity_gallery':GalleryForm,
    'Mailing':MailingForm,
    'Actualite':ActualiteForm,
}






