#!/usr/bin/env python2.7

import requests
import sys
import re

mainUrl = "http://www.searchenginesmarketer.com/list-of-university-and-college-websites/"

mainResponse = requests.get(mainUrl)
colleges = set()

for line in mainResponse.text.splitlines():
	match = re.findall('http://[^.]*.edu/', line)
	if len(match):
		colleges.add(match[0])

i = 0
for url in colleges:
	try:
		collegeResponse = requests.get(url)
	except requests.exceptions.ConnectionError:
		pass;
	
	if collegeResponse.status_code == 200:
		print url
	i = i + 1

print "{} college urls found".format(i)
	# infos = set() 
	# for line in collegeResponse.text.splitlines():
	# 	for p in re.findall('[^"]*/(about[^"]*)', line):
	# 		infos.add(url + p)
	# 	for p in(re.findall(url + '/about[^"]*', line)):
	# 		infos.add(p)
	# for x in infos:
	# 	print x

