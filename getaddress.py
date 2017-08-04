#!/usr/bin/python
import os, sys
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

key = os.getenv('key')

str = raw_input('Enter your location: \n')
		
	
def getlocation():
	"""This function returns the location of given places.
	Agrs:
		None.
		
	Return:
		lat(number): latitude of the location.
		lng(number): longtitude of the location.
	
	"""
	payload = {
			'query': str, 
			'key': key
	}
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	r = requests.get(url, params=payload)
	output = r.json()
	
	for item in output['results']:
		lat = item['geometry']['location']['lat']
		lng = item['geometry']['location']['lng']	
		
	return lat, lng
	

def result():
	
	"""This function returns a list of nearest electronic stores around given places.
	
	Agrs:
		None
		
	Return:
		result(string): list of nearest electronic stores, include: Store's name and address.
	
	"""
	loc = getlocation()
	lat = loc[0]
	lng = loc[1]
	payload = { 
			'radius': 4000, 
			'type': 'electronics_store', 
			'keyword': 'sieu+thi+dien+may', 
			'key': key
	}
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}'.format(lat, lng)
	r = requests.get(url, params=payload)
	output = r.json()
	
	print ('The list of nearest stores around your place: \n')
	for item in output['results']:
		name = (item['name'])
		address = (item['vicinity'])
		print ('Store: {}\tAddress: {}\n').format(name, address)
	
	return output['status']
	
print result()
