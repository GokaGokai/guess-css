#! /bin/python

import sys
from bs4 import BeautifulSoup

name = str(sys.argv[1])

with open("scrapped-html/" + name + ".html", "r") as f:
	scrappedDoc = BeautifulSoup(f, "html.parser")

output = scrappedDoc.find("style").string

with open("scrapped-css/" + name + ".css", "w") as file:
	file.write(str(output))