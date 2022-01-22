import csv

#These are the stringArray index/property mapping
# 00:'Title'
# 01:'CVSS Score'
# 02:'CVSS Vector'
# 03:'Priority'
# 04:'Impact'
# 05:'Probability'
# 06:'Host'
# 07:'IP'
# 08:'Port'
# 09:'Description'
# 10:'Remediation'
# 11:'Details'
# 12:'Target'
# 13:'Example
# 13:'Example'
# 14:'First Detected'
# 15:'Last Detected'
# 16:'Status'
# 17:'Notes'

class appCheckResult:
    def __init__(self, stringArray):
        self.Title = stringArray[0]
        self.Url = stringArray[6] + stringArray[12]
        self.IP = stringArray[7]
        self.Port = stringArray[8]
        self.Impact = stringArray[4]
        self.Rank = 0
        if(self.Impact == "High"):
            self.Rank = 1
        if(self.Impact == "Medium"):
            self.Rank = 2
        if(self.Impact == "Low"):
            self.Rank = 3
        if(self.Impact == "Info"):
            self.Rank = 4
        

    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, appCheckResult):
            return self.Title == other.Title and self.Url == other.Url and self.IP == other.IP and self.Port == other.Port and self.Impact == other.Impact 
    
def appCheckCSVtoObjectList(csvPath):
    resultsArray = []
    with open(csvPath, newline='') as f:
        reader = csv.reader(f)
        listOfArray = list(reader)
        for array in listOfArray:
            if listOfArray.index(array) != 0:
                resultsArray.append(appCheckResult(array))
        return resultsArray

def getSame(previousMonthsResultsArray, currentMonthsResultsArray):
    same = []
    for c in currentMonthsResultsArray:
        if c in previousMonthsResultsArray:
            same.append(c)
    return same

def getAdditions(previousMonthsResultsArray, currentMonthsResultsArray):
    additions = []
    for c in currentMonthsResultsArray:
        if c not in previousMonthsResultsArray:
            additions.append(c)
    return additions

def getRemovals(previousMonthsResultsArray, currentMonthsResultsArray):
    removals = []
    for p in previousMonthsResultsArray:
        if p not in currentMonthsResultsArray:
            removals.append(p)
    return removals

def printResultToFile(filePath, additions, removals, allResults, sameResults, delimiter):
    with open(filePath, "w+") as text_file:
        order = [("High",1), ("Medium", 2), ("Low", 3), ("Info", 4)]
        additions.sort(key=lambda x: (x.Rank, x.Title))
        removals.sort(key=lambda x: (x.Rank, x.Title))
        allResults.sort(key=lambda x: (x.Rank, x.Title))
        sameResults.sort(key=lambda x: (x.Rank, x.Title))

        text_file.write("sep=" + delimiter)
        text_file.write("\n\n\nAll Results:\n")
        text_file.write("Total:" + str(len(allResults)) + "\n")
        high = sum(p.Impact == "High" for p in allResults)
        med = sum(p.Impact == "Medium" for p in allResults)
        low = sum(p.Impact == "Low" for p in allResults)
        info = sum(p.Impact == "Info" for p in allResults)
        text_file.write("\n\n\nHigh:" + str(high) + delimiter + "Medium:" + str(med) + delimiter + "Low:" + str(low) + delimiter + "Info:" + str(info) + "\n")
        for a in allResults:
            text_file.write(a.Title + delimiter + a.Impact + delimiter + a.Url + delimiter + a.IP + delimiter + a.Port + "\n")

        text_file.write("\n\n\nRemovals:\n")
        text_file.write("Total:" + str(len(removals)) + "\n")
        for r in removals:
            text_file.write(r.Title + delimiter + r.Impact + delimiter + r.Url  + delimiter + r.IP + delimiter + r.Port + "\n")

        text_file.write("\n\n\nAdditions:\n")
        text_file.write("Total:" + str(len(additions)) + "\n")
        for a in additions:
            text_file.write(a.Title + delimiter + a.Impact + delimiter + a.Url + delimiter + a.IP + delimiter + a.Port + "\n")
        
        text_file.write("\n\n\nSame Results:\n")
        text_file.write("Total:" + str(len(sameResults)) + "\n")
        for s in sameResults:
            text_file.write(s.Title + delimiter + s.Impact + delimiter + s.Url + delimiter + s.IP + delimiter + s.Port + "\n")

def runComparerAgainstDirs(dirWithPreviousScans, dirWithCurrentScans, outputfile, delimiter):
    import glob
    filesPrevious = [f for f in glob.glob(dirWithPreviousScans + "**/*", recursive=True)]
    filesCurrent = [f for f in glob.glob(dirWithCurrentScans + "**/*", recursive=True)]
    
    #Construst one large object 
    allPrevious = []
    for x in filesPrevious:
        allPrevious += appCheckCSVtoObjectList(x)

    allCurrent = []
    for x in filesCurrent:
        allCurrent += appCheckCSVtoObjectList(x)

    additions = getAdditions(allPrevious, allCurrent)
    removals = getRemovals(allPrevious, allCurrent)
    same = getSame(allPrevious, allCurrent)
    printResultToFile(outputfile, additions, removals, allCurrent, same, delimiter)

    return [additions, removals, same, allCurrent]



def runMain(old,new,output, delimiter):
    currentMonthsResults = appCheckCSVtoObjectList(new)
    lastMonthsResults = appCheckCSVtoObjectList(old)
    additions = getAdditions(lastMonthsResults, currentMonthsResults)
    removals = getRemovals(lastMonthsResults, currentMonthsResults)
    same = getSame(lastMonthsResults, currentMonthsResults)
    printResultToFile(output, additions, removals, currentMonthsResults, same, delimiter)