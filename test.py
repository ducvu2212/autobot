import os
import json
import requests

key = os.getenv('key')
str = raw_input('Enter your location: \n')
payload = {
		'query': str, 
		'key': key
}
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	
	
	
def getlocation():
	"This function returns the location of a given place" 
	r = requests.get(url, params=payload)
	j = json.loads(r.text)
	
	if j['status'] == 'OK':
	
		for item in j['results']:
			lat = item['geometry']['location']['lat']
			lng = item['geometry']['location']['lng']
			# loc = item['geometry']['location']
	else: 
		print j['status']
	return lat, lng

l = getlocation()
lat = l[0]
lng = l[1]
payload2 = {
		# 'location': location, 
		'radius': 4000, 
		'type': 'electronics_store', 
		'keyword': 'sieu+thi+dien+may', 
		'key': key
}

url2 = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f' %(lat, lng))

def getaddress():
	"This function returns nearest addresses of a given location"
	r2 = requests.get(url2, params=payload2)
	return r2.url
	
print getaddress()
