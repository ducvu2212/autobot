import requests
import os
import key
import json

def getplaces() :
	"this function is used to get user's location detail" 
	key = os.environ.get('key')
	str = raw_input("Enter your location: \n") 
	r = requests.get('https://maps.googleapis.com'
			 '/maps/api/place/textsearch/json?query={}'
			 '&key={}'.format (str, key))
	return r.json()
		
