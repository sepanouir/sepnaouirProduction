from Sep import create_app,create
from config import ProductionConfig
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from Sep.models import Activity_user,db
from flask_mail import Mail, Message as Msg
from Sep.mail import mail,send_email_Activity
from flask import Flask, jsonify,request,session,redirect,url_for,render_template
from config import ProductionConfig

app=create_app(ProductionConfig)


sysAdmin=Admin(app)

sysAdmin.add_view(ModelView(Activity_user,db))












def build_sample_db():
	db.drop_all(app=app)
	db.create_all(app=app)


if __name__ == '__main__':
	# if not os.path.exists(db_uri):
		# build_sample_db()
	app.run()












  # const handle=()=>{ 
  #   setLoading(true)
  #   if(route.params['item'].submit){ 
  #   Alert.alert(
  #     "Sepanouir",
  #     "Etes-vous sûre que vous voulez annuler la participation",
  #     [
  #       {
  #         text: "Cancel",
  #         onPress: () => console.log("Cancel Pressed"),
  #         style: "cancel"
  #       },
  #       { text: "OK", onPress: () => annuler() }
  #     ]
  #   );
  #   }
  #   else{return participer()}
  # } 