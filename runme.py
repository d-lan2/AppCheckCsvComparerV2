from src.main import *

# runMain("C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/oct.csv",
# "C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/nov.csv",
# "C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/november/comparer/difference.csv", ",")

#The below are just placeholders
#runMain("oldScanLocationHere", "newScanLocationHere", "./output/Output.csv", ",")

runComparerAgainstDirs("C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/December/Exports",
"C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/January/Exports",
"C:/Users/dylan/Documents/Secarma/Reports/LMS Monthly/January/ComparerDiff/difference2.csv", "\t")
