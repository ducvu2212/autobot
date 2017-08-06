#!/usr/bin/python
import os, sys
import requests
# -*- coding: utf-8 -*-

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
	

def result(search_type = 'electronics_store', keyword = 'sieu+thi+dien+may'):
	
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
			'type': search_type, 
			'keyword': keyword, 
			'key': KEY
	}
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}'.format(lat, lng)
	r = requests.get(url, params=payload)
	output = r.json()
	
	print ('The list of nearest stores around your place: \n')
	from texttable import Texttable
	t = Texttable()
	t.add_row(['Store', 'Address'])
	
	for item in output['results']:
		name = item['name']
		address = item['vicinity']
		t.add_row([name, address])
	t.set_deco(t.HEADER | t.VLINES | t.HLINES)
	t.set_cols_width([60, 80])
	t.set_cols_align(['l','l'])
	t.set_cols_valign(['t','t'])
	print t.draw().encode('utf-8')
	
	return output['status']
	
print result()
