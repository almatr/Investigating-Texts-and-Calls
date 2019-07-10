"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def createUniqueList(firstList, secondList):
    """
    Create an empty list called uniqueList and add elements that are not already in the list
    When loop is done take the length of the uniqueList and return the number
    """
    uniqueList = []
    for eachList in (firstList, secondList):
        for item in eachList:
            if item[0] not in uniqueList:
                uniqueList.append(item[0])
            if item[1] not in uniqueList:
                uniqueList.append(item[1])

    return len(uniqueList)





"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

print("There are", createUniqueList(texts, calls), "different telephone numbers in the records.")






