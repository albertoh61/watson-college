#!/usr/bin/env python2.7

import requests
import sys
import re

mainUrl = "http://www.searchenginesmarketer.com/list-of-university-and-college-websites/"

mainResponse = requests.get(mainUrl)
colleges = []

for line in mainResponse.text.splitlines():
	match = re.findall('http://[^.]*.edu/', line)
	if len(match):
		colleges.append(match[0])

for url in colleges:
	print url;
	# collegeUrls = []
	# collegeResponse = requests.get(url)
	
	# infos = set() 
	# for line in collegeResponse.text.splitlines():
	# 	for p in re.findall('[^"]*/(about[^"]*)', line):
	# 		infos.add(url + p)
	# 	for p in(re.findall(url + '/about[^"]*', line)):
	# 		infos.add(p)
	# for x in infos:
	# 	print x

# This was as far as I got until I realized I couldn't do much with the about urls
# I just picked one sepcific college to test on, but ideally it would test all by altering the condition in line 14
