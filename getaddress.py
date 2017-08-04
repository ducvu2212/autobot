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
	output = json.loads(r.text)

	if output['status'] == 'OK':
	
		for item in output['results']:
			lat = item['geometry']['location']['lat']
			lng = item['geometry']['location']['lng']
			
	else: 
		return output['status']
		
	return lat, lng
	

def result():
	
	"""This function returns a list of nearest electronic stores around given places.
	
	Agrs:
		None
		
	Return:
		Param1(result): list of nearest electronic stores, include: Store's name and address.
	
	"""
	loc = getlocation()
	lat = loc[0]
	lng = loc[1]
	payload = { 
			'radius': 4000, 
			'type': type, 
			'keyword': keyword, 
			'key': key
	}
	url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}'.format(lat, lng))
	r = requests.get(url, params=payload)
	output = json.loads(r.text)
	
	if output['status'] == 'OK':
		print ('The list of nearest stores around your place: \n')
		
		for item in output['results']:
			name = (item['name'])
			address = (item['vicinity'])
			print ('Store: {}\tAddress: {}\n').format(name, address)
			
	else:
		return output['status']
	return output['status']
	
print result()
