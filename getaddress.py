#!/usr/bin/python
import os, sys
import json
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

key = os.getenv('key')
type = os.getenv('type')
keyword = os.getenv('keyword')

str = raw_input('Enter your location: \n')

def geturl1():
	"This function returns the URL for location search via API"
	payload = {
			'query': str, 
			'key': key
	}
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	return url, payload
	
def getlocation():
	"This function returns the location of a given place" 
	u = geturl1()
	r = requests.get(u[0], params=u[1])
	output = json.loads(r.text)

	if output['status'] == 'OK':
	
		for item in output['results']:
			lat = item['geometry']['location']['lat']
			lng = item['geometry']['location']['lng']
			
	else: 
		print output['status']
	return lat, lng

def geturl2():

	loc = getlocation()
	lat = loc[0]
	lng = loc[1]
	payload2 = { 
			'radius': 4000, 
			'type': type, 
			'keyword': keyword, 
			'key': key
	}

	url2 = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f' %(lat, lng))
	return url2, payload2

def result():
	"This function returns nearest addresses of a given location"
	u = geturl2()
	r = requests.get(u[0], params=u[1])
	output = json.loads(r.text)
	
	if output['status'] == 'OK':
		for item in output['results']:
			name = (item['name'])
			address = (item['vicinity'])
			print ('Store: {} \t Address: {}\n').format(name, address)
	else:
		print output['status']
	
print result()
