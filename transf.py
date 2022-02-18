#! /bin/python

from bs4 import BeautifulSoup
from random import shuffle
import re
import sys

# Shuffle function
RE_GARBLE = re.compile(r"\b(\w)(\w+)(\w)\b")

def garble_word(match):
    first, middle, last = match.groups()

    middle = list(middle)
    shuffle(middle)

    return first + ''.join(middle) + last


def garble(sentence):
    return RE_GARBLE.sub(garble_word, sentence)

# TO DO:
# Add ARGUMENT for HTML names
# Input

namefile = str(sys.argv[1])

with open("scrapped-html/" + namefile + ".html", "r") as f:
	scrappedDoc = BeautifulSoup(f, "html.parser")

with open("skeleton-html/index.html", "r") as f2:
	skeletonDoc = BeautifulSoup(f2, "html.parser")

with open("skeleton-html/indexSol.html", "r") as f3:
	skeletonSolDoc = BeautifulSoup(f3, "html.parser")

# TO DO:
# Need to find the counter, hard coded for now
strongTitle1 = skeletonDoc.find_all("strong")[0]
strongTitle1.string = "test 1" 


# Previous and Next
previous = scrappedDoc.find("a", text="<==")
next = scrappedDoc.find("a", text="==>")

if previous != None:
	skeletonDoc.find_all("a")[0]["href"] = previous["href"]

if next != None:
	skeletonDoc.find_all("a")[1]["href"] = next["href"]

# Extract elements
style = scrappedDoc.find("style")
cssScrapped = scrappedDoc.find_all("pre")[0].string
htmlScrapped = scrappedDoc.find_all("pre")[1].string
solutionScrapped = scrappedDoc.find(class_="testText")

# Modify skeleton-html-sol
fieldSol = skeletonSolDoc.find_all("pre")
cssFieldSol = fieldSol[0]
htmlFieldSol = fieldSol[1]
solutionFieldSol = skeletonSolDoc.find(class_="sol")
styleFieldSol = skeletonSolDoc.find("style")

cssFieldSol.string = cssScrapped
htmlFieldSol.string = htmlScrapped
solutionFieldSol.contents = solutionScrapped.contents
styleFieldSol.contents=style.contents

# Modify skeleton-html
field = skeletonDoc.find_all("pre")
cssField = field[0]
htmlField = field[1]
solutionField = skeletonDoc.find(class_="sol")
styleField = skeletonDoc.find("style")

solButton = skeletonDoc.find_all("a")[2]["href"] = namefile + "-Sol.html"

cssField.string = cssScrapped
htmlField.string = garble(htmlScrapped)
solutionField.contents = solutionScrapped.contents
# styleField.contents=style.contents

# TO DO:
# Undo shuffle for sol
temp = solutionScrapped
for child in temp.find_all():
	if child.string != None: 
		child.string = garble(child.string)

# Output
with open("transf-html/" + namefile + ".html" , "w") as file:
	file.write(str(skeletonDoc))

with open("transf-html/" + namefile + "-Sol.html", "w") as file:
	file.write(str(skeletonSolDoc))
