import random
Az = [chr(65+i) for i in range(26)]
Az.extend([str(i) for i in range(10)])
import requests

# print(Az)
def generate(n=6):
	z=''
	for i in range(6):
		z+=random.choice(Az)
	return z
api_key='57a4d05d-7095-4a6c-8a35-35fd9c4b4d8f'
email = "abderafiechairi01@gmail.com"

def check_email(email,apikey):
	response = requests.get(
	    "https://isitarealemail.com/api/email/validate",
	    params = {'email': email},
	     headers = {'Authorization': "Bearer " + api_key })

	status = response.json()['status']
	if status == "valid":
		return True
	elif status == "invalid":
		return False
	else:
		raise Exception(401)