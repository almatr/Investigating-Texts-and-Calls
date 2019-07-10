"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def findMaxTime(telList):

    my_dict = {}

    for record in telList:
        if record[0] in my_dict.keys():
            value = my_dict[record[0]]
            value += int(record[3])
            my_dict[record[0]] = value
        else:
            my_dict[record[0]] = int(record[3])
        if record[1] in my_dict.keys():
            value = my_dict[record[1]]
            value += int(record[3])
            my_dict[record[1]] = value
        else:
            my_dict[record[1]] = int(record[3])

    biggestKey = max(my_dict, key=my_dict.get)
    timeInSec = my_dict[biggestKey]

    return (biggestKey,timeInSec)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


recordWithMax = findMaxTime(calls)
print(recordWithMax[0], "spent the longest time,", recordWithMax[1], "seconds, on the phone during September 2016.")


