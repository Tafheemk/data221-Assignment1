# Tafheem Khan 30219735
# Data 221 Assignment_1 Question 6 "Distribution Analysis"
# Need to define a function which recives a list of numbers and returns a dict where each key is a unique value from said list, each value is the % of elements in the list that are <= the key and must be sorted by key before being returned
def DistributionAnalysis(Numbers):
    ResultingDict = {}
    TotalNums = len(Numbers)

    # Get unique values and sort them
    Unique_values = sorted(set(Numbers))

    # Calculate percentages
    for value in Unique_values:
        Count = sum(1 for n in Numbers if n <= value)
        ResultingDict[value] = (Count / TotalNums) * 100

    return ResultingDict

