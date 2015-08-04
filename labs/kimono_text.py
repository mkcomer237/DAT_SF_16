import json
import urllib

api_key = 'Rm9Em3kl0DCGV5SWQ01wf0ZUG4JufvxV'

startyear = 2002
endyear = 2002
url = "https://www.kimonolabs.com/api/ondemand/7q3deoj4?apikey=%s&release_date=%s" % (api_key, startyear)
#url = "https://www.kimonolabs.com/api/7q3deoj4?apikey=%s" % (api_key)


print url


raw = urllib.urlopen(url)
print raw.readlines()
results = json.load(urllib.urlopen(url))

#print "crap"
print results