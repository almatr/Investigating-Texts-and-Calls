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

# Identify possible marketers
def possTelemarkterers(calls, texts):

    #reduce duplicates for the loop and result
    allCalls = list(zip(*calls))
    allTexts = list(zip(*texts))
    outgoingCalls = set(allCalls[0])
    incomingCalls = set(allCalls[1])
    outgoingTexts = set(allTexts[0])
    incomingTexts = set(allTexts[1])

    result = []
    for record in outgoingCalls:
        if record not in incomingCalls and record not in outgoingTexts and record not in incomingTexts:
            result.append(record)

    result.sort()

    return result

#print numbers
def printNums(listOfNums):

    print("These numbers could be telemarketers: ")
    for num in listOfNums:
        print(num)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

printNums(possTelemarkterers(calls,texts))



