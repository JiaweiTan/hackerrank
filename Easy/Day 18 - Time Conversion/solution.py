#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeFormat = s[-2:]
    convertedTime = s[:-2]
    hour = s[:2]
    if timeFormat == 'PM' and s[:2] != '12':
        hour = str(int(s[:2]) + 12)
    elif timeFormat == 'AM' and s[:2] == "12":
        hour = '00'
    convertedTime = hour[:2] + convertedTime[2:]
    return convertedTime

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
