#!/usr/bin/env python2.7

import requests
import zipfile
import atexit
import shutil
import tempfile
import StringIO

url = "https://ope.ed.gov/accreditation/datafiles/accreditation_2016_03.zip"
fileName = "accreditation_2016_03.csv"
print "Downloading {}...".format(url)
response = requests.get(url, stream=True)
z = zipfile.ZipFile(StringIO.StringIO(response.content))

schools = set()
with z.open(fileName) as fs:
	for line in fs:
		l = line.split(",");
		if not l[1].startswith('"'): 
			schools.add(l[1])

for school in schools:
	print school

