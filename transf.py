#! /bin/python

from logging.config import stopListening
from bs4 import BeautifulSoup
from random import shuffle
import re


RE_GARBLE = re.compile(r"\b(\w)(\w+)(\w)\b")


def garble_word(match):
    first, middle, last = match.groups()

    middle = list(middle)
    shuffle(middle)

    return first + ''.join(middle) + last


def garble(sentence):
    return RE_GARBLE.sub(garble_word, sentence)

# Only the first test for now
with open("guess-css/scrapped-html/css3-modsel-1.html", "r") as f:
	scrappedDoc = BeautifulSoup(f, "html.parser")

with open("guess-css/skeleton-html/index.html", "r") as f2:
	skeletonDoc = BeautifulSoup(f2, "html.parser")


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


# Solution doesn't work
field = skeletonDoc.find_all("pre")
cssField = field[0]
htmlField = field[1]
# solutionField = skeletonDoc.findAll(class_="test-box")[2]
solutionField = skeletonDoc.find(class_="sol")
styleField = skeletonDoc.find("style")

style = scrappedDoc.find("style")
cssScrapped = scrappedDoc.find_all("pre")[0].string
htmlScrapped = scrappedDoc.find_all("pre")[1].string
solutionScrapped = scrappedDoc.find(class_="testText")

# print(solutionField)
cssField.string = cssScrapped
htmlField.string = garble(htmlScrapped)
solutionField.contents = solutionScrapped.contents
# styleField[1]['style']=style.contents
styleField.contents=style.contents
# solutionField['style']=style.contents

for child in solutionScrapped.find_all():
	if child.string != None: 
		child.string = garble(child.string)

with open("guess-css/transf-html/css3-modsel-1.html", "w") as file:
	file.write(str(skeletonDoc))
