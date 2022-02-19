#!/bin/python
import sys
from bs4 import BeautifulSoup

# Input
repInput = str(sys.argv[1])
repOutput = str(sys.argv[2])
namefile = str(sys.argv[3])

with open(repInput + "/" + namefile + ".html", "r") as f:
	scrappedDoc = BeautifulSoup(f, "html.parser")

# Output
output = scrappedDoc.find("style").string

with open(repOutput + "/" + namefile + ".css", "w") as file:
	file.write(str(output))
