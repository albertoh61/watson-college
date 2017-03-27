#!/usr/bin/env python2.7

import atexit
import os
import re
import shutil
import sys
import tempfile

import requests

FIELD = "title"
LIMIT = 10
SUBREDDIT = "college"
REG = False

def usage(status=0):
    print '''Usage: {} [ -f FIELD -s SUBREDDIT ] regex
    	-f FIELD        Which field to search (default: {})
    	-n LIMIT        Limit number of articles to report (default: {})
    	-s SUBREDDIT    Which subreddit to search (default: {})'''.format(
        os.path.basename(sys.argv[0]),FIELD, LIMIT, SUBREDDIT
    )
    sys.exit(status)

args = sys.argv[1:]

while len(args) and len(args[0]) > 1:
    arg = args.pop(0)
    if arg == '-f':
	FIELD = args.pop(0)
    elif arg == '-n':
	LIMIT = int(args.pop(0))
    elif arg == '-s':
	SUBREDDIT = args.pop(0)
    elif arg == '-h':
	usage(1)
    elif not arg.startswith('-'):
	REGEX = arg
	REG = True

URL = 'https://www.reddit.com/r/' + SUBREDDIT + '/.json'
headers = {'user-agent': 'reddit-{}'.format(os.environ['USER'])}

myFile = requests.get(URL, headers=headers)

titles = []
authors = []
links = []
nums = []
num = 1

for post in myFile.json()["data"]["children"]:
	fields = post["data"]
	try:
		link = fields["permalink"]
		URL = 'https://www.reddit.com' + link
		titl = fields["title"]
		auth = fields["author"]
		if FIELD == "title" and REG:
			if re.search(REGEX, titl):
				titles.append(titl)
		else:
			titles.append(titl)
		if FIELD == "author" and REG:
			if re.search(REGEX, auth):
				authors.append(auth)
		else:
			authors.append(auth)
		if FIELD == "link" and REG:
			if re.search(REGEX, link):
				links.append(link)
		else:
			links.append(link)
		nums.append(num)
		num = num + 1
	except KeyError:
		print 'Invalid field: ' + FIELD
		sys.exit(1)

for titl, author, link, x , y in zip(titles, authors, links, nums, range(0,LIMIT)):
	print str(x).ljust(4) + 'Title: '.ljust(2) + '  ' + titl
	print 'Author: '.rjust(12) + '  ' + author
	print 'Link: '.rjust(10) + '  ' + link
