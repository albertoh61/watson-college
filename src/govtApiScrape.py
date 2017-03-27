#!/usr/bin/env python2.7

import requests
APIKEY = "api_key=LqM5NhDNLbD12MklskDjXVoB0nYTkhe1LNiucQd6"

for i in range(1, 387):
	response = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools/?" + APIKEY + "&_page=" + str(i))
	
	try:
		for x in response.json()['results']:
			print x['school']['name']
	except ValueError:
		pass;
