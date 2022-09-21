# from models import *
from .models import *

def create(app):
	with app.app_context():
		db.create_all()
		db.session.commit()
		Rubriques=[
			Rubrique(name="SEPSorcier"),
			Rubrique(name="Quotidien")
		]
		db.session.add_all(Rubriques)
		db.session.commit()
		Sections=[

			Section(value='Que ce que la SEP ?',name='Que_ce_que_la_sep',rubrique_id=Rubrique.getId('SEPSorcier')),
			Section(value='Presentation SEP',name='Presentation_sep',rubrique_id=Rubrique.getId('SEPSorcier')),
			Section(value='Sportez-vous bien',name='Sportez_vous_bien',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='La SEP gourmande',name='Sep_gourmande',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='SEP et emploi',name='Sep_et_emploi',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='SEP et famille',name='Sep_et_famille',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='Le stress…à mieux gérer',name='Stress_gerer',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='La SEP invisible',name='Sep_invisible',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='Témoignages',name='Temoignages',rubrique_id=Rubrique.getId('Quotidien')),
			Section(value='Actualités',name='Actualites'),
			Section(value='Partenaires',name='Partenaires')
	]
		db.session.add_all(Sections)
		db.session.commit()
		Items=[
			Item(name='Généralités',details='',section_id=Section.getSection('Que_ce_que_la_sep').id),
			Item(name='Causes et symptômes',details='',section_id=Section.getSection('Que_ce_que_la_sep').id),
			Item(name='Diagnostic',details='',section_id=Section.getSection('Que_ce_que_la_sep').id),
			Item(name='Traitement',details='',section_id=Section.getSection('Que_ce_que_la_sep').id),
			Item(name='Genèse de SEPanouir',details='',section_id=Section.getSection('Presentation_sep').id),
			Item(name='Mot du président',details='',section_id=Section.getSection('Presentation_sep').id),
			Item(name='Rejoindre SEPanouir ',details='',section_id=Section.getSection('Presentation_sep').id),

	]
		db.session.add_all(Items)
		db.session.commit()

 


