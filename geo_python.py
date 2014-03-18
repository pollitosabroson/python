import urllib2
import pprint
import json
add = "Zocalo, mexico"
add = urllib2.quote(add)
geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&region=mx" % add
print geocode_url
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())
pprint.pprint(jsonResponse) 