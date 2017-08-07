# -*- coding: utf-8 -*-
#!/usr/bin/python
import os, sys
import requests

KEY = os.getenv('key')
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
			'key': KEY
	}
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
	r = requests.get(url, params=payload)
	output = r.json()
	
	for item in output['results']:
		lat = item['geometry']['location']['lat']
		lng = item['geometry']['location']['lng']	
		
	return lat, lng
	

def store_list(search_type = 'electronics_store', keyword = 'sieu+thi+dien+may'):
	
	"""This function returns a list of nearest electronic stores around given places.
	
	Params:
		search_type(string): parameter in url
		keyword(string): parameter in url
		
	Return:
		store_data(string): return a list of store's name and address
	
	"""
	lat = getlocation()[0]
	lng = getlocation()[1]
	payload = { 
			'radius': 4000, 
			'type': search_type, 
			'keyword': keyword, 
			'key': KEY
	}
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}'.format(lat, lng)
	r = requests.get(url, params=payload)
	output = r.json()
	
	for item in output['results']:
		name = item['name']
		address = item['vicinity']
		store_data = [name, address]
		yield store_data
		
print (list(store_list(10)))
