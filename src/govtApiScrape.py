#!/usr/bin/env python2.7

import requests
APIKEY = "api_key=LqM5NhDNLbD12MklskDjXVoB0nYTkhe1LNiucQd6"

response = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools/?" + APIKEY + "&")
print len(response.json()['results'])
for x in response.json()['results']:
	print x['school']['name']
