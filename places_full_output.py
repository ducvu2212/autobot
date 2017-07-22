import requests

r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=20.99527,105.855783&radius=2000&type=electronics_store&keyword=si%C3%AAu+thi%CC%A3+%C4%91i%C3%AA%CC%A3n+ma%CC%81y&key=AIzaSyDXmq7S5L3w9otA1HmYziQ77f8oTgltzp0')
#r.json()
print r.text
