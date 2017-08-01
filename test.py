import os
import json
import requests

key = os.getenv('key')

def url1(): 
	"This function returns GG Search API URL"
	
	str = raw_input('Enter your location: \n')
	payload = {
		'query': str, 
		'key': key
	}
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	
	
	
def getlocation():
	"This function returns the location of a given place" 
	a = url1()
	url = a['url']
	r = requests.get(url, params=payload)
	j = json.loads(r.text)
	
	if j['status'] == 'OK':
	
		for item in j['results']:
			lat = item['geometry']['location']['lat']
			lng = item['geometry']['location']['lng']
	else: 
		print j['status']

def url2(): 
	location = getlocation()
	lat = location['lat']
	lng = location['lng']
	payload2 = {
		'location': [lat, lng], 
		'radius': 4000, 
		'type': 'electronics_store', 
		'keyword': 'sieu+thi+dien+may', 
		'key': key
	}

	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

def getaddress():
	"This function returns nearest addresses of a given location"
	url = url2()
	r2 = requests.get(url2, params=payload2)
	return r2.url
	
print getaddress()