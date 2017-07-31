import os
import json
import requests

key = os.getenv('key')
str = raw_input('Enter your location: \n')
#payload = {'str': str, 'key': key}
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str + key

def getplaces() :
	"This function returns the location of a given place" 
	r = requests.get(url)
	j = json.loads(r.text)
	lat = j['latitude']
	lon = j['longitude']
	print ('latitude is: \n', lat)
	print ('longtitude is: \n', long)

print getplaces()		
