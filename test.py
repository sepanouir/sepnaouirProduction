from Sep import *
from config import ProductionConfig
import datetime
app=create_app(ProductionConfig)

users=[User(public_id="730d6e4c-27ea-11ed-82b7-7a63971df0dd",nom ='El',prenom ='Basma',date_naissance =datetime.date(1991,8,17),debut_SEP ='2021',ntel ='',sexe ='Féminin',metier ="Fonctionnaire ",loisirs ='Lecture ',ville_residence ='Rabat',grand_ville ='Rabat',medecin_traitant ='Professeur Rahmani',traitement ='Avonex',couvMed ='Aucun',email ='Ibtissamerrai17@gmail.com',password ='Basma@1991',auth =True,sep =True,viewed =True,active =True,recovery ='OTNF6B'),
User(public_id="61fa5266-2aa4-11ed-bb69-86dde92ac64c",nom ='Ilham',prenom ='Ilham',date_naissance =datetime.date(1981,5,25),debut_SEP ='',ntel ='',sexe ='Féminin',metier ="Professeur ",loisirs ='Voyage,randonnée ',ville_residence ='Rabat',grand_ville ='',medecin_traitant ='',traitement ='',couvMed ='Aucun',email ='Ilham.laouzi@gmail.com',password ='Laouzi1981',auth =False,sep =False,viewed =True,active =False,recovery ='AIU9HA'),
User(public_id="77c39c9e-2494-11ed-b8ec-2e163162aad4",nom ='Bounouar',prenom ='Loubna',date_naissance =datetime.date(1975,8,2),debut_SEP ='2018',ntel ='0641041671',sexe ='Féminin',metier ="Responsable logistique",loisirs ='Yoga',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Pr slassi ilham',traitement ='Aubagio',couvMed ='Mutuelle privée',email ='lo.bounouar@hotmail.fr',password ='loubna1975',auth =True,sep =True,viewed =True,active =True,recovery ='LXZUDZ'),
User(public_id="2d5f7098-2489-11ed-9732-2e163162aad4",nom ='Ezzouine ',prenom ='Aïcha ',date_naissance =datetime.date(1984,7,11),debut_SEP ='2013',ntel ='0662889665',sexe ='Féminin',metier ="Enseignemente",loisirs ='Voyage et sport',ville_residence ='Mohammedia ',grand_ville ='Mohammédia',medecin_traitant ='Dr Araqi houssaini Adik',traitement ='Gilenya',couvMed ='CNSS',email ='aezzouine84@gmail.com',password ='kenza2015',auth =True,sep =True,viewed =True,active =True,recovery ='N7EJON'),
User(public_id="5775045a-24d0-11ed-96ca-ca5c85e0160f",nom ='Bouchane',prenom ='Salah Eddine',date_naissance =datetime.date(1989,9,29),debut_SEP ='2014',ntel ='0670071927',sexe ='Masculin',metier ="Enseignant",loisirs ='Velo jardinage',ville_residence ='Témara',grand_ville ='Rabat',medecin_traitant ='Pr. Motii',traitement ='Gilenya',couvMed ='CNOPS',email ='Salah.bc@gmail.com',password ='sep@nouir2022',auth =True,sep =True,viewed =True,active =True,recovery ='5GA6MX'),        
User(public_id="e60dad70-2539-11ed-bbff-461f7ac2a4a6",nom ='Asmaa',prenom ='Bouchara ',date_naissance =datetime.date(1966,10,17),debut_SEP ='1997',ntel ='',sexe ='Féminin',metier ="Aucun ",loisirs ='A remplir ',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='A remplir ',traitement ='Aucun',couvMed ='Aucun',email ='asmaa.bouchara@gmail.com',password ='123456789A',auth =True,sep =True,viewed =True,active =True,recovery ='69ME1K'),
User(public_id="0577316c-2545-11ed-bbff-461f7ac2a4a6",nom ='Meniam ',prenom ='Soumia',date_naissance =datetime.date(1990,5,27),debut_SEP ='2010',ntel ='0634483011',sexe ='Féminin',metier ="étudiante",loisirs ='Le dessin ',ville_residence ='Mohammedia ',grand_ville ='Mohammédia',medecin_traitant ='Dr Rajae Rabhi ',traitement ='Gilenya',couvMed ='CNOPS',email ='Soumiameniam2@gmail.com',password ='sarachaimaemaissae',auth =False,sep =True,viewed =True,active =True,recovery ='X1UJL3'),
User(public_id="6678b87a-207f-11ed-856c-1aa12d4e7a4f",nom ='Abouzia',prenom ='Chaimaa',date_naissance =datetime.date(1986,4,13),debut_SEP ='2021',ntel ='0610101026',sexe ='Féminin',metier ="Responsable administratif Ste informatique ",loisirs ='Sport , voyage, music',ville_residence ='Rabat',grand_ville ='Rabat',medecin_traitant ='Dr ouafaa Mouti',traitement ='Gilenya',couvMed ='CNSS',email ='Chaimaa.abouzia@gmail.com',password ='13@chaimaa',auth =True,sep =True,viewed =None,active =True,recovery ='V8S1VS'),
User(public_id="64b65516-25e2-11ed-a75d-dafdad6fd4c2",nom ='Babarami ',prenom ='Ismail',date_naissance =datetime.date(2008,1,4),debut_SEP ='2022',ntel ='0601561987',sexe ='Masculin',metier ="Étudiant ",loisirs ='Foot',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Dr slassi',traitement ='Rebif',couvMed ='Mutuelle privée',email ='Lamyae.nassir@gmail.com',password ='Ismail2022',auth =True,sep =True,viewed =True,active =False,recovery ='WG6OPN'),    
User(public_id="4b96c1c6-2711-11ed-9ce0-c6f7231ff8c8",nom ='Kharbane',prenom ='Najib',date_naissance =datetime.date(1996,1,1),debut_SEP ='2019',ntel ='',sexe ='Masculin',metier ="Consultant BI",loisirs ='Judo et basketball',ville_residence ='Chambery',grand_ville ='Sefrou',medecin_traitant ='Marcel sebastien',traitement ='Tysabri',couvMed ='Ameli',email ='Najib.kharbane@gmail.com',password ='Thewordis123.',auth =True,sep =True,viewed =True,active =True,recovery ='150D4P'),   
User(public_id="d4883cd0-2923-11ed-a95f-024013f58422",nom ='CHMITE',prenom ='Assia',date_naissance =datetime.date(1990,12,10),debut_SEP ='2007',ntel ='',sexe ='Féminin',metier ="Contrôleur de gestion ",loisirs ='Vélo ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Ezzoubi mounir',traitement ='Aucun',couvMed ='Aucun',email ='Assia.chmite@gmail.com',password ='Kakashi123.',auth =False,sep =True,viewed =True,active =True,recovery ='HKEWHG'),        
User(public_id="64cf1a30-28a6-11ed-9648-7a1c5ff3162b",nom ='Assaoui ',prenom ='Khadija ',date_naissance =datetime.date(1982,2,17),debut_SEP ='2015',ntel ='0657024121',sexe ='Féminin',metier ="Secrétaire ",loisirs ='La marche ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Professeur moutawakil Bouchra ',traitement ='Avonex',couvMed ='CNSS',email ='assaoui.casalabpalmier@gmail.com',password ='assaouisep1982',auth =False,sep =True,viewed =True,active =False,recovery ='D4C5U3'),
User(public_id="2d0fb966-2adf-11ed-b16a-ee3b78326723",nom ='FARJIA',prenom ='Laila',date_naissance =datetime.date(1955,3,16),debut_SEP ='1997',ntel ='0661751971',sexe ='Féminin',metier ="Retraitée",loisirs ='Peinture, voyages  et chorale.',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Pr SLASSI',traitement ='Tysabri',couvMed ='CNSS',email ='Loubaba555@hotmail.com',password ='Chama1918',auth =False,sep =True,viewed =True,active =True,recovery ='WCSWCO'),
User(public_id="1995a4dc-2c23-11ed-9346-faa9cfb8f74c",nom ='SAMMAK',prenom ='Fatima zahra',date_naissance =datetime.date(1997,6,12),debut_SEP ='2021',ntel ='0662043490',sexe ='Féminin',metier ="Conseillère de clientèle dans une banque",loisirs ='marche, faire le tour des restau, Music',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr ARAQUI ADEL ',traitement ='Autre',couvMed ='Mutuelle privée',email ='fatisammak@gmail.com',password ='Fati1997',auth =True,sep =True,viewed =True,active =True,recovery ='Q1HTXH'),
User(public_id="cffdcb46-2bab-11ed-ac41-6209733e9288",nom ='Benkirane ',prenom ='Khadija',date_naissance =datetime.date(1996,5,8),debut_SEP ='2021',ntel ='0600608722',sexe ='Féminin',metier ="Chirurgien dentiste ",loisirs ='Dessin',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Professeur Slassi',traitement ='Rituximab',couvMed ='Aucun',email ='khadija.benkirane1996@gmail.com',password ='aqwzsxaqwzsx123+',auth =True,sep =True,viewed =True,active =False,recovery ='RX2M3D'),
User(public_id="52f57e62-2090-11ed-856c-1aa12d4e7a4f",nom ='Miss',prenom ='Sb',date_naissance =datetime.date(1992,3,19),debut_SEP ='2019',ntel ='0662248243',sexe ='Féminin',metier ="Banquière ",loisirs ='Sport ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Dr Midafi Naila ',traitement ='Aubagio',couvMed ='Cmim',email ='Sbouiri@outlook.com',password ='DAvidson1992',auth =True,sep =True,viewed =None,active =True,recovery ='K21V14'),
User(public_id="6209d9cc-2075-11ed-a9d0-1aa12d4e7a4f",nom ='Boumart',prenom ='Imane',date_naissance =datetime.date(1989,8,10),debut_SEP ='2014',ntel ='0669211655',sexe ='Féminin',metier ="Cadre en industrie pharmaceutique",loisirs ='Danser ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Mr Iraqi ',traitement ='Aucun',couvMed ='Aucun',email ='imaneboumart@hotmail.com',password ='baculovirus',auth =True,sep =True,viewed =True,active =True,recovery 
='8TTKNV'),
User(public_id="836b3112-2078-11ed-856c-1aa12d4e7a4f",nom ='Ben zairh',prenom ='Mustapha ',date_naissance =datetime.date(1997,4,12),debut_SEP ='2021',ntel ='0766555597',sexe ='Masculin',metier ="Étudiant ",loisirs ='Voyage ',ville_residence ='Nancy',grand_ville ='Casablanca',medecin_traitant ='Colombo',traitement ='Ocrevus',couvMed ='Aucun',email ='mustapha.benzairh@gmail.com',password ='stoof_123',auth =True,sep =True,viewed =None,active =True,recovery ='4U9GHC'),
User(public_id="637f4646-2090-11ed-856c-1aa12d4e7a4f",nom ='Ballouki',prenom ='Adel',date_naissance =datetime.date(1987,12,14),debut_SEP ='2011',ntel ='0667059351',sexe ='Masculin',metier ="Ingenieur informatique",loisirs ='Musiue natation ',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Professeur Slassi',traitement ='Tysabri',couvMed ='CNSS',email ='Adel.ballouki@gmail.com',password ='Adillevis1*',auth =True,sep =True,viewed =True,active =True,recovery ='I6QXFE'),
User(public_id="dbfb3524-2092-11ed-a9d0-1aa12d4e7a4f",nom ='Elb',prenom ='Soumaya',date_naissance =datetime.date(1990,12,2),debut_SEP ='',ntel ='0615062164',sexe ='Féminin',metier ="supply chain",loisirs ='Musique',ville_residence ='Marseille',grand_ville ='',medecin_traitant ='',traitement ='',couvMed ='Aucun',email ='Soumaya.elb@hotmail.fr',password ='Maroc2020',auth =True,sep =False,viewed =True,active =True,recovery ='GJ81FX'),
User(public_id="11332f30-20ac-11ed-b6e7-5a5f4e82a263",nom ='Louizi ',prenom ='Asmaa ',date_naissance =datetime.date(1990,11,29),debut_SEP ='2014',ntel ='0691719400',sexe ='Féminin',metier ="Comptable ",loisirs ='Voyage,lecture ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Docteur Adil Iraqi houssaini ',traitement ='Gilenya',couvMed ='CNSS',email ='louizi.asmaa@gmail.com',password ='29RN3a82',auth =True,sep =True,viewed =True,active =True,recovery ='SSWYJ0'),
User(public_id="367d8396-216d-11ed-816a-a68d2ec5a5f0",nom ='Zian',prenom ='Yousra',date_naissance =datetime.date(1992,4,20),debut_SEP ='2019',ntel ='0666950099',sexe ='Féminin',metier ="Ingénieur industriel",loisirs ='No longer know',ville_residence ='Tetouan',grand_ville ='Tétouan',medecin_traitant ='Mrani Alia',traitement ='Betaferon',couvMed ='Mutuelle privée',email ='Yousrazian@gmail.com',password ='ibrahim2017',auth =False,sep =True,viewed =True,active =True,recovery ='TN7S1J'),
User(public_id="594c7d4e-2174-11ed-816a-a68d2ec5a5f0",nom ='Mokaddem',prenom ='Sofia',date_naissance =datetime.date(1988,6,7),debut_SEP ='2015',ntel ='0620767143',sexe ='Féminin',metier ="Cadre",loisirs ='Tout et rien',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr naila midafi',traitement ='Aucun',couvMed ='Aucun',email ='Sofia.mokaddem@gmail.com',password ='bidou33.m',auth =True,sep =True,viewed =True,active =True,recovery ='R3Q38O'),
User(public_id="db9abcfe-2177-11ed-92f8-a68d2ec5a5f0",nom ='Houdou',prenom ='Tarik',date_naissance =datetime.date(1981,6,13),debut_SEP ='2008',ntel ='0661858353',sexe ='Masculin',metier ="Coordinateur",loisirs ='La marche',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Mouti',traitement ='Avonex',couvMed ='CNSS',email ='Tarikhoudou@gmail.com',password ='secommeca22',auth =True,sep =True,viewed =True,active =True,recovery ='4H5X6K'),
User(public_id="91948394-2175-11ed-816a-a68d2ec5a5f0",nom ='Touahar ',prenom ='Asmae',date_naissance =datetime.date(1991,5,14),debut_SEP ='2008',ntel ='0697825216',sexe ='Féminin',metier ="Dentiste ",loisirs ='Yoga ,coloriage, lecture ',ville_residence ='Sidi kacem',grand_ville ='Sidi Kacem',medecin_traitant ='Aucun ',traitement ='Aucun',couvMed ='CNOPS',email ='Asmaetouahar1@gmail.com',password ='asmaeasmae31',auth =True,sep =True,viewed =None,active =True,recovery ='NLP00M'),
User(public_id="d5144226-2175-11ed-816a-a68d2ec5a5f0",nom ='Benriyene',prenom ='Salwa',date_naissance =datetime.date(1986,9,11),debut_SEP ='2003',ntel ='0664887575',sexe ='Féminin',metier ="Ingénieur d'état en informatique",loisirs ='Randonnées, voyages',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr slassi',traitement ='Avonex',couvMed ='Atlanta sanad',email ='Salwabenriyene@gmail.com',password ='salwa2026',auth =True,sep =True,viewed =True,active =True,recovery ='5V5YLO'),
User(public_id="5e8a7cc0-2179-11ed-816a-a68d2ec5a5f0",nom ='Korich',prenom ='Mohamed nazih',date_naissance =datetime.date(1991,12,22),debut_SEP ='2018',ntel ='0671245494',sexe ='Masculin',metier ="Employé ",loisirs ='Football',ville_residence ='Tanger',grand_ville ='Tanger',medecin_traitant ='Docteur fadil hicham',traitement ='Tysabri',couvMed ='CNSS',email ='Korichnazih@gmail.com',password ='Nazih123',auth =True,sep =True,viewed =True,active =True,recovery ='GW3ICH'),       
User(public_id="0920f04c-217a-11ed-816a-a68d2ec5a5f0",nom ='Bahta ',prenom ='Youssef ',date_naissance =datetime.date(1994,7,21),debut_SEP ='2013',ntel ='0706853737',sexe ='Masculin',metier ="Commercial ",loisirs ='Cinéphile ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Slassi ',traitement ='Ocrevus',couvMed ='CNSS',email ='youssefbahta@gmail.com',password ='youssef1994',auth =True,sep =True,viewed =None,active =True,recovery ='HAFDY7'),        
User(public_id="1eb6c170-217a-11ed-92f8-a68d2ec5a5f0",nom ='Mastour ',prenom ='Abdelmajid ',date_naissance =datetime.date(1990,6,24),debut_SEP ='2013',ntel ='0614883359',sexe ='Masculin',metier ="Banquier",loisirs ='Divers',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Dr. Midafi naila',traitement ='Aucun',couvMed ='Mutuelle privée',email ='Abdelmajid.mastour@hotmail.com',password ='Majido5971130',auth =True,sep =True,viewed =True,active =True,recovery ='D47PXA'),
User(public_id="a0136700-217a-11ed-92f8-a68d2ec5a5f0",nom ='YAALAOUI ',prenom ='Fouad',date_naissance =datetime.date(1991,10,13),debut_SEP ='2018',ntel ='0677010784',sexe ='Masculin',metier ="Sans",loisirs ='Pêche',ville_residence ='Sidi rahal',grand_ville ='Casablanca',medecin_traitant ='Dr bouchra moutawakil',traitement ='Gilenya',couvMed ='CNSS',email ='Yaalaoui.fouad07@gmail.com',password ='Sepanouir07',auth =True,sep =True,viewed =True,active =True,recovery ='2R3N0F'),  
User(public_id="c3157e62-217c-11ed-92f8-a68d2ec5a5f0",nom ='Baïna',prenom ='Mouna',date_naissance =datetime.date(1985,11,21),debut_SEP ='2018',ntel ='0670287054',sexe ='Féminin',metier ="Femme au foyer",loisirs ='Natation',ville_residence ='Tamesna',grand_ville ='Rabat',medecin_traitant ='Benaaboud bouchra',traitement 
='Rebif',couvMed ='CNOPS',email ='mounabaina@gmail.com',password ='malaktahaziad3',auth =True,sep =True,viewed =True,active =True,recovery ='QLTTUL'),
User(public_id="825f37fc-2184-11ed-92f8-a68d2ec5a5f0",nom ='Cherkaoui',prenom ='Oumaima',date_naissance =datetime.date(1980,1,5),debut_SEP ='2011',ntel ='0600636021',sexe ='Féminin',metier ="Mère au foyer",loisirs ='Sport',ville_residence ='Mohammedia ',grand_ville ='Mohammédia',medecin_traitant ='Iraqui Houssaini Adil',traitement ='Ocrevus',couvMed ='CNOPS',email ='oumaimac80@gmail.com',password ='kamilina80',auth =True,sep =True,viewed =True,active =True,recovery ='GMTPNF'),
User(public_id="06f6ec5a-218d-11ed-8fa2-ee6f8954e473",nom ='Nejjar',prenom ='Oussama',date_naissance =datetime.date(1974,12,31),debut_SEP ='1975',ntel ='0664344344',sexe ='Masculin',metier ="Employé de banque",loisirs ='.',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr Adil laraqui',traitement ='Ocrevus',couvMed ='Cmim',email ='onejjar@gmail.com',password ='Raja491:',auth =True,sep =True,viewed =True,active =True,recovery ='F2IR3J'),
User(public_id="f1c214d0-2192-11ed-95a8-ee6f8954e473",nom ='Mouti',prenom ='Ouafa',date_naissance =datetime.date(1972,4,10),debut_SEP ='',ntel ='0667225471',sexe ='Féminin',metier ="Médecin neurologue",loisirs ='Sport',ville_residence ='Rabat',grand_ville ='',medecin_traitant ='',traitement ='',couvMed ='Aucun',email ='ouafamouti@yahoo.fr',password ='Avril1972',auth =False,sep =False,viewed =None,active =True,recovery ='1HE041'),
User(public_id="a3a0d722-2a2b-11ed-a3b3-66b6636c80b1",nom ='Tazi',prenom ='Ilham',date_naissance =datetime.date(1984,11,22),debut_SEP ='2001',ntel ='',sexe ='Féminin',metier ="Encadrants pedagogique",loisirs ='Music, cuisine',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr iraki ',traitement ='Gilenya',couvMed ='CNSS',email ='taziilham@gmail.com',password ='ilham1984',auth =False,sep =True,viewed =True,active =True,recovery ='2CHE19'),
User(public_id="52535a58-2c73-11ed-ac76-42672c45f3c2",nom ='A',prenom ='L',date_naissance =datetime.date(1900,7,20),debut_SEP ='2017',ntel ='0660949613',sexe ='Féminin',metier ="CM",loisirs ='Lec',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr Adil ARAQI',traitement ='Rebif',couvMed ='CNSS',email ='loubna.aallam@gmail.com',password ='Loubna20',auth =True,sep =True,viewed =True,active =True,recovery ='LNQLEN'),
User(public_id="c7698dae-2196-11ed-95ec-32c2414907b7",nom ='Faroini',prenom ='Wafaa',date_naissance =datetime.date(1995,5,18),debut_SEP ='2015',ntel ='0607639319',sexe ='Féminin',metier ="Ingenieure genie civil ",loisirs ='Sport',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Dr. Ilham Slassi',traitement ='Ocrevus',couvMed ='CNSS',email ='wafaa.faroini1@gmail.com',password ='casa101010',auth =True,sep =True,viewed =True,active =True,recovery ='MQ1LV8'),
User(public_id="6924d494-2a2c-11ed-a611-66b6636c80b1",nom ='Iman',prenom ='Iman',date_naissance =datetime.date(1989,9,1),debut_SEP ='2017',ntel ='',sexe ='Féminin',metier ="Ingénieur informatique",loisirs ='Aucun',ville_residence ='Sale',grand_ville ='Salé',medecin_traitant ='Ouhabi Hamid',traitement ='Aubagio',couvMed ='CNSS',email ='iman407fr@hotmail.com',password ='Capgemini01!',auth =False,sep =True,viewed =True,active =True,recovery ='LMS20T'),
User(public_id="ddd6065c-248a-11ed-9732-2e163162aad4",nom ='Hala',prenom ='Harzaoui ',date_naissance =datetime.date(1986,5,22),debut_SEP ='2018',ntel ='0767244355',sexe ='Féminin',metier ="English teacher ",loisirs ='Tv',ville_residence ='Mohammedia ',grand_ville ='Casablanca',medecin_traitant ='Dr Rafei ',traitement ='Aucun',couvMed ='Aucun',email ='harzaouihh@gmail.com',password ='Freedom4058',auth =True,sep =True,viewed =None,active =True,recovery ='KJPAX5'),
User(public_id="e07df02c-2539-11ed-90b0-461f7ac2a4a6",nom ='BENABDALLAH',prenom ='Mariem',date_naissance =datetime.date(1995,8,19),debut_SEP ='2020',ntel ='0659737897',sexe ='Féminin',metier ="Étudiante ",loisirs ='Musique ',ville_residence ='Sala el jadida ',grand_ville ='Salé',medecin_traitant ='BENOMAR ',traitement 
='Aucun',couvMed ='Aucun',email ='benabmariem133@gmail.com',password ='123456789.mimi',auth =True,sep =True,viewed =None,active =True,recovery ='4ETP0N'),      
User(public_id="6a9b405a-2a3c-11ed-a611-66b6636c80b1",nom ='Bendarkawi',prenom ='Zineb ',date_naissance =datetime.date(1989,9,21),debut_SEP ='2017',ntel ='0608496698',sexe ='Féminin',metier ="Banquiere",loisirs ='Lecture',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Dr khalidi',traitement ='Ocrevus',couvMed ='CMIM',email ='Zineb.bendarkawi@hotmail.com',password ='Juliana21',auth =False,sep =True,viewed =True,active =True,recovery ='RJHBHI'),    
User(public_id="ac6b12fe-24c3-11ed-a64b-060b3e04c3f7",nom ='Hana',prenom ='Salma',date_naissance =datetime.date(2003,9,12),debut_SEP ='2019',ntel ='0665055684',sexe ='Féminin',metier ="Étudiante ",loisirs ='Dessin ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Hicham el othmani',traitement ='Rebif',couvMed ='Mutuelle privée',email ='uuygiyf@gmail.com',password ='0665055684salma',auth =True,sep =True,viewed =True,active =False,recovery ='473J9J'),
User(public_id="88e1d3ca-2533-11ed-90b0-461f7ac2a4a6",nom ='Abbad',prenom ='Hayat',date_naissance =datetime.date(1984,1,6),debut_SEP ='2020',ntel ='0665463347',sexe ='Féminin',metier ="Fonctionnaire ",loisirs ='Danse voyage ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Dr iraqui houssaini adil',traitement ='Rebif',couvMed ='CNOPS',email ='Hyattoamir@gmail.com',password ='Sephyatt2022',auth =True,sep =True,viewed =True,active =False,recovery ='MGKJOI'),
User(public_id="915f0888-2565-11ed-805a-ca6d956279dd",nom ='EL GHAZLANI',prenom ='Ilham',date_naissance =datetime.date(1983,5,8),debut_SEP ='2013',ntel ='0679266969',sexe ='Féminin',metier ="Pensionné ",loisirs ='Lecture',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Prof EL MOUTAWAKIL Bouchra',traitement ='Rebif',couvMed ='CNSS',email ='i.elghazlani@gmail.com',password ='ilhamdream',auth =True,sep =True,viewed =True,active =True,recovery ='IE1ABC'),
User(public_id="3873a0dc-2662-11ed-9736-9edd1acc21bc",nom ='Baissoune ',prenom ='Chaimaa',date_naissance =datetime.date(1992,7,30),debut_SEP ='2022',ntel ='0601595275',sexe ='Féminin',metier ="Assistante technique ",loisirs ='Sport, le.voyage, la création et le savoir faire ',ville_residence ='Casablanca ',grand_ville 
='Casablanca',medecin_traitant ='Docteur Elharizi Ilham ',traitement ='Rebif',couvMed ='CNSS',email ='baissounechaimaa@gmail.com',password ='LAROUSSE.2022.ncc',auth =True,sep =True,viewed =True,active =True,recovery ='JIJJ6B'),
User(public_id="08e9be1e-2793-11ed-bac5-728328ef60a2",nom ='Benyaich',prenom ='Otman',date_naissance =datetime.date(1965,2,8),debut_SEP ='2015',ntel ='0661268346',sexe ='Masculin',metier ="Financier",loisirs ='Danse',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Pr Slassi',traitement ='Aubagio',couvMed ='Mutuelle privée',email ='Otmanbeny@hotmail.com',password ='Ob08021965',auth =True,sep =True,viewed =None,active =True,recovery ='EU57TQ'),       
User(public_id="f84094d0-2aca-11ed-87bc-d64dd1ce0de7",nom ='Karim',prenom ='Meryem',date_naissance =datetime.date(1985,6,28),debut_SEP ='2020',ntel ='0669124123',sexe ='Féminin',metier ="Commercial",loisirs ='Vouage',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Pr slassi',traitement ='Gilenya',couvMed ='Aucun',email ='Karimmeryem548@gmail.com',password ='28@2008.',auth =True,sep =True,viewed =True,active =True,recovery ='SZR232'),
User(public_id="5ba1f9ec-232d-11ed-bc4c-1ede2e09bfe6",nom ='Gannoune',prenom ='Aziza',date_naissance =datetime.date(1986,8,24),debut_SEP ='2009',ntel ='',sexe ='Feminin',metier ="Ingénieur ",loisirs ='Yoga / Vélo ',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Pr Slassi ',traitement ='Aucun',couvMed ='CFE',email ='Aziza.gannoune@gmail.com',password ='Azizag86',auth =False,sep =True,viewed =None,active =True,recovery ='FHR6CT'),
User(public_id="3fe6fbe8-2c48-11ed-8dbc-c648874c5c64",nom ='FAHSI ',prenom ='Soundouss ',date_naissance =datetime.date(1976,10,10),debut_SEP ='2018',ntel ='0661506953',sexe ='Féminin',metier ="Fonctionnaire ",loisirs ='Musique/marche ',ville_residence ='Rabat ',grand_ville ='Rabat',medecin_traitant ='Dr.Moutie ',traitement ='Aubagio',couvMed ='CNOPS',email ='soundouss.fahsi@gmail.com',password ='Lasou3876',auth =False,sep =True,viewed =True,active =True,recovery ='QW8BY0'),  
User(public_id="e7147e0e-3341-11ed-aeaa-26d6ea9f7acb",nom ='Gasmi',prenom ='Madiha',date_naissance =datetime.date(1980,1,1),debut_SEP ='2018',ntel ='',sexe ='Féminin',metier ="A remplir ",loisirs ='A remplir',ville_residence ='Rabat ',grand_ville ='Rabat',medecin_traitant ='A remplir ',traitement ='Aucun',couvMed ='Aucun',email ='Madiha.gasmi@gmail.com',password ='123456789M',auth =True,sep =True,viewed =False,active =False,recovery ='ZJU3NM'),
User(public_id="88250510-31c7-11ed-aba7-6e1be438bf33",nom ='Chairi',prenom ='Abderafie',date_naissance =datetime.date(2002,1,1),debut_SEP ='2017',ntel ='',sexe 
='Masculin',metier ="Prof",loisirs ='Sport',ville_residence ='Fnideq',grand_ville ='Tétouan',medecin_traitant ='Zahraoui',traitement ='Aucun',couvMed ='Aucun',email ='abderafiechairi02@gmail.com',password ='123123123',auth =True,sep =True,viewed =None,active =True,recovery ='YHPXKN'),
User(public_id="fe8fb27a-31dd-11ed-bda7-6e1be438bf33",nom ='Ahizoune',prenom ='Salma',date_naissance =datetime.date(1990,12,7),debut_SEP ='2017',ntel ='0661251918',sexe ='Féminin',metier ="Cadre IT",loisirs ='Voyage/musique',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Professeur Slassi',traitement ='Aubagio',couvMed ='Mutuelle privée',email ='Ahizounesalma1@gmail.com',password ='Supinf0*',auth =True,sep =True,viewed =False,active =True,recovery 
='WUSJRR'),
User(public_id="a4d7712e-31fa-11ed-862f-12064c542ce3",nom ='Trioui',prenom ='Fatima Zahra ',date_naissance =datetime.date(1984,11,12),debut_SEP ='2019',ntel ='0707071409',sexe ='Féminin',metier ="Enseignante",loisirs ='..',ville_residence ='Tanger ',grand_ville ='Tanger',medecin_traitant ='NA',traitement ='Aucun',couvMed ='Axa et AMO',email ='tetem3oui@gmail.com',password ='tetemsep',auth =True,sep =True,viewed =False,active =True,recovery ='LAYYI3'),
User(public_id="3fec83e4-2534-11ed-90b0-461f7ac2a4a6",nom ='Malika ',prenom ='Guerraoui ',date_naissance =datetime.date(1980,10,1),debut_SEP ='1996',ntel ='',sexe ='Féminin',metier ="Cadre supérieur ",loisirs ='Sport, yoga, méditation ',ville_residence ='Rabat ',grand_ville ='Rabat',medecin_traitant ='Al Zemmouri Khadija ',traitement ='Aucun',couvMed ='CNOPS',email ='mguerraouister@gmail.com',password ='Bakizati@1234',auth =True,sep =True,viewed =None,active =True,recovery ='VH8D4Q'),
User(public_id="159bf19c-237c-11ed-8d12-16ee9eec16fa",nom ='Wahbi Mernissi',prenom ='Mehdi ',date_naissance =datetime.date(1986,7,9),debut_SEP ='',ntel ='',sexe ='Masculin',metier ="Ingénieur ",loisirs ='Foot',ville_residence ='Casablanca',grand_ville ='',medecin_traitant ='',traitement ='',couvMed ='Aucun',email ='Wahbi.mehdi@gmail.com',password ='123456789M',auth =False,sep =False,viewed =None,active =True,recovery ='MPW364'),
User(public_id="30a3026e-328b-11ed-8b49-ee4d20e60946",nom ='Benriyene',prenom ='Salwa',date_naissance =datetime.date(1986,9,11),debut_SEP ='2003',ntel ='0664887575',sexe ='Féminin',metier ="Formatrice",loisirs ='Musique randonnee',ville_residence ='Casa',grand_ville ='Chefchaouen',medecin_traitant ='Dr slassi',traitement ='Avonex',couvMed ='Atlanta sanad',email ='Sousou3sm@hotmail.com',password ='Msteam222',auth =True,sep =True,viewed =False,active =False,recovery ='WQHMFX'),User(public_id="329fc090-3289-11ed-9cce-ee4d20e60946",nom ='Hamidat',prenom ='Samia',date_naissance =datetime.date(1991,5,14),debut_SEP ='2020',ntel ='0631859025',sexe ='Féminin',metier ="Infirmiére",loisirs ='Sport',ville_residence ='Salé',grand_ville ='Salé',medecin_traitant ='Dr benaboud',traitement ='Aubagio',couvMed ='CNOPS',email ='htsamia68@gmail.com',password ='Samiaakram',auth =False,sep =True,viewed =None,active =True,recovery ='FOV7PT'),
User(public_id="f73d5c76-301a-11ed-a402-f255a0562624",nom ='Boumadi',prenom ='Kaoutar',date_naissance =datetime.date(1987,8,16),debut_SEP ='2015',ntel ='0600600661',sexe ='Féminin',metier ="Consultante RH",loisirs ='Lecture, écriture, musique',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Adil Iraqi Houssaini',traitement ='Ocrevus',couvMed ='CNSS',email ='kaoutarboumadi@gmail.com',password ='Maj+14683',auth =True,sep =True,viewed =True,active =True,recovery ='XZ3X7K'),
User(public_id="9299afe0-3042-11ed-b0e2-dafaa727f4fc",nom ='Benlemlih ',prenom ='Meryem',date_naissance =datetime.date(1995,6,24),debut_SEP ='',ntel ='',sexe ='Féminin',metier ="Ingénieur ",loisirs ='Sport et voyage ',ville_residence ='Casablanca ',grand_ville ='',medecin_traitant ='',traitement ='',couvMed ='Aucun',email ='Meryembenlemlih06@gmail.com',password ='MERYEMSEPANOUIR',auth =True,sep =False,viewed =True,active =False,recovery ='5MANWJ'),
User(public_id="9815eee2-31ce-11ed-bda7-6e1be438bf33",nom ='Chakib ',prenom ='Karima',date_naissance =datetime.date(1962,9,30),debut_SEP ='2001',ntel ='0667434670',sexe ='Féminin',metier ="Retraitée ",loisirs ='Cuisine ',ville_residence ='Casablanca',grand_ville ='Casablanca',medecin_traitant ='Slassi',traitement ='Autre',couvMed ='CNOPS',email ='karima.chakib62@gmail.com',password ='aziza2020',auth =True,sep =True,viewed =True,active =False,recovery ='RVO7O5'),
User(public_id="dc23d872-3432-11ed-9cc5-e6c8f40bfbf9",nom ='Adaoui ',prenom ='Sanaa ',date_naissance =datetime.date(1980,12,26),debut_SEP ='2007',ntel ='0669735860',sexe ='Féminin',metier ="Dessin de bâtiment d'architecture ",loisirs ='Voyage, lecture, natation et la danse ',ville_residence ='Casablanca ',grand_ville ='Casablanca',medecin_traitant ='Rafai',traitement ='Aucun',couvMed ='CNSS',email ='adaouisanaa.spirale@gmail.com',password ='fatimahjoube123',auth =True,sep =True,viewed =False,active =True,recovery ='ODF32M'),
User(public_id="a6c7aaa2-3430-11ed-a7f8-e6c8f40bfbf9",nom ='Mansouri',prenom ='Naoual',date_naissance =datetime.date(1975,5,20),debut_SEP ='2012',ntel ='0661059367',sexe ='Féminin',metier ="Ingénieur",loisirs ='Voyage',ville_residence ='Kenitra',grand_ville ='Kénitra',medecin_traitant ='Dr Mrani Alia',traitement ='Avonex',couvMed ='Aucun',email ='naoual.mansouri@gmail.com',password ='Hana2006',auth =True,sep =True,viewed =False,active =True,recovery ='1IIAHV'),
]



# import Dat
def myDate(d):
	return f'datetime.date({d.year},{d.month},{d.day})'

with app.app_context():
	# a=User.query.all()
	# req = '['
	# for i in a:
	# 	req+=f"""User(public_id="{i.public_id}",nom ='{i.nom}',prenom ='{i.prenom}',date_naissance ={myDate(i.date_naissance)},debut_SEP ='{i.debut_SEP}',ntel ='{i.ntel}',sexe ='{i.sexe}',metier ="{i.metier}",loisirs ='{i.loisirs}',ville_residence ='{i.ville_residence}',grand_ville ='{i.grand_ville}',medecin_traitant ='{i.medecin_traitant}',traitement ='{i.traitement}',couvMed ='{i.couvMed}',email ='{i.email}',password ='{i.password}',auth ={i.auth},sep ={i.sep},viewed ={i.viewed},active ={i.active},recovery ='{i.recovery}'),\n"""
	# req+=']'
	# print(req)
	

# 	# i=users[0]
# 	# print(i)
# 	# # db.session.add(i)
	for i in users:
		db.session.add(i)
	db.session.commit()
	print('done')