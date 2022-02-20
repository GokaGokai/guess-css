import glob
import re

#Places all error txt files into one txt file
errorFiles = glob.glob("error-css/*.txt")

with open("errorReport.txt", "wb") as eR:
    for f in errorFiles:
        with open(f, "rb") as rF:
            eR.write(rF.read())

#finds index of an error in an array
def findIndex(tab,error):
    for index in range(len(tab)):
        if tab[index] == error:
            return index
    return -1

#extract error types and which files they are associated to
errorName = []
errorFiles = []

with open("errorReport.txt", "rt") as errorFile:
    for line in errorFile:
        errorType = re.search("Error:(.*?)\.", line).group(1)
        errorFile = re.search("scrapped-css/(.*?)\ ", line).group(1)
        if errorType not in errorName:
            errorFiles.append([errorFile])
            errorName.append(errorType)
        else:
            errorIndex = findIndex(errorName,errorType)
            errorFiles[errorIndex].append(errorFile)

#writes the report
reportContents = ""
with open("report.txt", "w") as reportFile:
    for err in range(len(errorName)):
        print(errorName[err])
        reportContents = "Error: " + errorName[err] + ".\nfiles: "
        print(errorFiles[err])
        reportContents += ", ".join(errorFiles[err])
        reportContents += "\n"
        reportFile.write(reportContents)
    