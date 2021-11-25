from src.main import *

# runMain("C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/oct.csv",
# "C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/nov.csv",
# "C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/difference.csv", ",")

#The below are just placeholders
#runMain("oldScanLocationHere", "newScanLocationHere", "./output/Output.csv", ",")

runComparerAgainstDirs("C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/allScansOld",
"C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/allScansNew",
"C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/AllScansDifference.csv", ",")
