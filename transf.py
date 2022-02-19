#!/bin/python
from bs4 import BeautifulSoup
from random import shuffle
import re
import sys

# Input
repInput = str(sys.argv[1])
repOutput = str(sys.argv[2])
namefile = str(sys.argv[3])

with open(repInput + "/" + namefile + ".html", "r") as f:
	scrappedDoc = BeautifulSoup(f, "html.parser")

with open(repInput + "/" + namefile + ".html", "r") as ft:
	scrappedDocTemp = BeautifulSoup(ft, "html.parser")

with open("skeleton-html/index.html", "r") as f2:
	skeletonDoc = BeautifulSoup(f2, "html.parser")

with open("skeleton-html/indexSol.html", "r") as f3:
	skeletonSolDoc = BeautifulSoup(f3, "html.parser")
	

# Shuffle function
RE_GARBLE = re.compile(r"\b(\w)(\w+)(\w)\b")

def garble_word(match):
    first, middle, last = match.groups()

    middle = list(middle)
    shuffle(middle)

    return first + ''.join(middle) + last

def garble(sentence):
    return RE_GARBLE.sub(garble_word, sentence)


# Current test name display
strongTitle1 = skeletonDoc.find_all("strong")[0]
strongTitle1.string = namefile 

# Previous and Next buttons
previous = scrappedDoc.find("a", text="<==")
next = scrappedDoc.find("a", text="==>")

if previous != None:
	skeletonDoc.find_all("a")[0]["href"] = previous["href"]
	skeletonSolDoc.find_all("a")[0]["href"] = previous["href"]

if next != None:
	skeletonDoc.find_all("a")[1]["href"] = next["href"]
	skeletonSolDoc.find_all("a")[1]["href"] = next["href"]


# Extract elements from scrapped html
style = scrappedDoc.find("style")
cssScrapped = scrappedDoc.find_all("pre")[0].string
htmlScrapped = scrappedDoc.find_all("pre")[1].string
solutionScrapped = scrappedDoc.find(class_="testText")
solutionScrappedTemp = scrappedDocTemp.find(class_="testText")


# Modify skeleton-html-sol
fieldSol = skeletonSolDoc.find_all("pre")
cssFieldSol = fieldSol[0]
htmlFieldSol = fieldSol[1]
solutionFieldSol = skeletonSolDoc.find(class_="sol")

cssFieldSol.string = cssScrapped
htmlFieldSol.string = htmlScrapped
solutionFieldSol.contents = solutionScrappedTemp.contents

# Linking CSS sheets
skeletonSolDoc.find_all("link")[2]["href"] = "css/" + namefile + "-Sol.css"

# Hide Solution Button
skeletonSolDoc.find_all("a")[2]["href"] = namefile + ".html"


# Modify skeleton-html
field = skeletonDoc.find_all("pre")
cssField = field[0]
htmlField = field[1]
solutionField = skeletonDoc.find(class_="sol")

solButton = skeletonDoc.find_all("a")[2]["href"] = namefile + "-Sol.html"

cssField.string = cssScrapped

# Apply Shuffle in HTML and Solution Field
htmlField.string = garble(htmlScrapped)

solutionField.contents = solutionScrapped.contents
for child in solutionScrapped.find_all():
	if child.string != None: 
		child.string = garble(child.string)


# Output HTMLs
with open(repOutput + "/" + namefile + ".html" , "w") as file:
	file.write(str(skeletonDoc))

with open(repOutput + "/" + namefile + "-Sol.html", "w") as file:
	file.write(str(skeletonSolDoc))

# Output SASS
sass = ".sol {"+style.string+"}"

with open(repOutput + "/sass/" + namefile + "-Sol.scss", "w") as file:
	file.write(str(sass))
