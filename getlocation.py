import os
import json
import requests

key = os.getenv('key')
str = raw_input('Enter your location: \n')
payload = {'query': str, 'key': key}
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

def getlocation() :
	"This function returns the location of a given place" 
	r = requests.get(url, params=payload)
	j = json.loads(r.text)
	
	if j['status'] == 'OK':
	
		for item in j['results']:
			lat = item['geometry']['location']['lat']
			lng = item['geometry']['location']['lng']
	else: 
		print j['status']
	
	return lat, lng
	
print getlocation()
