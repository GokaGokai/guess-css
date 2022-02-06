from asyncio.windows_events import NULL
from bs4 import BeautifulSoup

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
field = skeletonDoc.find_all("p")
cssField = field[1]
htmlField = field[2]
solutionField = skeletonDoc.findAll(class_="test-box")[2]

style = scrappedDoc.find("style")
cssScrapped = scrappedDoc.find_all("pre")[0].string
htmlScrapped = scrappedDoc.find_all("pre")[1].string
# solutionScrapped = scrappedDoc.find(class_="testText").contents[1]

cssField.string = cssScrapped
htmlField.string = htmlScrapped
# solutionField.string.insert_after("test")
# print(solutionField)


with open("guess-css/transf-html/css3-modsel-1.html", "w") as file:
	file.write(str(skeletonDoc))
