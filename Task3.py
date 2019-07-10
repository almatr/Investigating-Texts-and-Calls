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

#Function for part A (takes a list of all calls and returns sorted list of area codes of Bangalore fixed numbers, mobile
# numbers and telemarketers numbers)
def allBanCalls(allCalls):

    listOfCodes = []
    bangalore_prefix = "(080)"

    # Find codes that match the criteria and add to the list
    for record in allCalls:
        if (record[0].find(bangalore_prefix) > -1) :
            if (record[1][0] == "(" and record[1][1] == "0"):               #fixed lines
                if (record[1][1:record[1].index(")")]) not in listOfCodes:
                    listOfCodes.append(record[1][1:record[1].index(")")])
            if record[1][0] in ("7", "8", "9") and record[1][5] == " ":     #mobile numbers
                if record[1][:4] not in listOfCodes:
                    listOfCodes.append(record[1][:4])
            if record[1][:3] == "140" and " " not in record[1]:              #telemarketers
                if record[1][:3] not in listOfCodes:
                    listOfCodes.append(record[1][:3])

    listOfCodes.sort()

    return listOfCodes

#Function for part A (a function that prints a list)
def printAreaCodes(listOfCodes):

    print("The numbers called by people in Bangalore have codes:")
    for areaCode in listOfCodes:
        print(areaCode)




#Function for part B - This functions takes all calls and finds the percentage of calls from fixed lines in Bangalore
# to other fixed lines in Bangalore
def percentageOfCalls(allCalls):

    allFixed = 0;
    toFixed = 0;
    percentResult = 0;
    bangalore_prefix = "(080)"

    for record in allCalls:
        if (record[0].find(bangalore_prefix) > -1) :
            allFixed +=1
            if (record[1].find(bangalore_prefix) > -1) :
                toFixed +=1

    percentResult = (toFixed / allFixed) * 100

    return round(percentResult, 2)


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# part A
printAreaCodes(allBanCalls(calls))


# part B
percentageOfCalls(calls)
print(percentageOfCalls(calls),  "percent of calls from fixed lines in Bangalore are calls to other fixed lines in "
                                 "Bangalore.")
