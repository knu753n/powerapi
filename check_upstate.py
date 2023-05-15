import requests
import os

try:
	r = requests.get('http://10.0.0.158')

	state = r.status_code

except Exception as e:
	state = 404

if state == 404:
	os.system("python3 /home/tibber/app.py")
