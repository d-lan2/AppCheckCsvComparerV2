from ..src.main import *

def test_test_can_run():
    x = 1
    assert x == 1

def test_can_correctly_convert_csv():
    results = appCheckCSVtoObjectList("./tests/test_data/Sept_Scan.csv")
    assert len(results) == 275

def test_can_correctly_calculation_same():
    currentMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Sept_Scan.csv")
    lastMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Aug_Scan.csv")
    same = getSame(lastMonthsResults, currentMonthsResults)
    additions = getAdditions(lastMonthsResults, currentMonthsResults)
    assert len(same) == 223
    assert len(same) == len(currentMonthsResults) - len(additions)

def test_can_correctly_calculate_additions():
    currentMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Sept_Scan.csv")
    lastMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Aug_Scan.csv")
    additions = getAdditions(lastMonthsResults, currentMonthsResults)
    assert len(additions) == 52

def test_can_correctly_calculate_removals_simple():
    currentMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Sept_Scan.csv")
    lastMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Aug_Scan.csv")
    removals = getRemovals(lastMonthsResults, currentMonthsResults)
    assert len(removals) == 207

def test_can_correctly_calculate():
    currentMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Sept_Scan.csv")
    lastMonthsResults = appCheckCSVtoObjectList("./tests/test_data/Aug_Scan.csv")
    removals = getRemovals(lastMonthsResults, currentMonthsResults)
    additions = getAdditions(lastMonthsResults, currentMonthsResults)
    same = getSame(lastMonthsResults, currentMonthsResults)
    assert len(currentMonthsResults) == len(lastMonthsResults) + len(additions) - len(removals)
    assert len(lastMonthsResults) == len(currentMonthsResults) - len(additions) + len(removals)
    assert len(same) == len(lastMonthsResults) - len(removals)


def test_can_correctly_calculate_when_concatting_scan_results():
    results = runComparerAgainstDirs("./tests/test_data/dirtest/previous", "./tests/test_data/dirtest/current", "./output/dirtest/output.csv", ",")
    additions, removals, same, allCurrent = results
    assert len(additions) == 1
    assert len(removals) == 2
    assert len(same) == 12
    assert len(additions) + len(same) + len(removals)  == len(allCurrent) + 2 #+2 to account for removals

    #Discrepency analysis
        # #Here i am reverting this months set calculations to get last months
    # #copy items
    # dis = currentMonthsResults.copy()
    # #readd the removed items
    # dis.extend(removals)
    # #remove the added items
    # for r in additions:
    #     dis.remove(r)
    # #dis SHOULD now be the same last months list but we know its not
    # #now we can identify the discrepencies by subtracting last months list from dis
    # for r in lastMonthsResults:
    #     dis.remove(r)
    # #count should be 5
    # x = len(dis)
    # #wtf are those 5 results tho?

    # #Ends up equalling 5
    # last = 0
    #  #Ends up equalling 5
    # current = 0
    # adds = 0
    # rems = 0
    # #Ends up equalling 5
    # sam = 0
    # for d in dis:
    #     if d in lastMonthsResults:
    #         last += 1
    #     if d in currentMonthsResults:
    #         current += 1
    #     if d in additions:
    #         adds += 1
    #     if d in removals:
    #         rems += 1
    #     if d in same:
    #         sam += 1
    # #the discrepencies are present in last months list, this months list and the same lists. How many of each occurance in each list?

    # last2 = 0
    # current2 = 0
    # sam2 = 0
    # for d in dis:
    #     if d in lastMonthsResults:
    #         last2 += lastMonthsResults.count(d)
    #     if d in currentMonthsResults:
    #         current2 += currentMonthsResults.count(d)
    #     if d in same:
    #         sam2 += same.count(d)
    # #results: this months and current list contain dupes

    
    
    

