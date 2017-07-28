import requests
import os
import json


key = os.getenv('key')
str = raw_input('Enter your location: \n')
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str + key


def getplaces() :
	"This function returns the location of a given place" 
	r = requests.get(url)
	output_dict = json.loads(r)
	#output_dict.get('location')
	return output_dict['location']

print getplaces()		
