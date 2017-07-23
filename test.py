import requests

def getplaces( str ):
	"this function send google API URL as a request" 
	"to get a list of defined places"

	str = raw_input ("Please enter your location: \n")

	r = requests.get('https://maps.googleapis.com'
	'/maps/api/place/textsearch/json?query=%s'
	'&key=AIzaSyBu4EbNUZUfGzeFdvjXdIs2GhN_BPRKRQ8' % str)

	print r.text
		
