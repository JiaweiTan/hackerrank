#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    noOfHighBreaks = 0
    noOfLowBreaks = 0
    highest = scores[0]
    lowest = scores[0]
    for n in range(1,len(scores)):
        if scores[n] > highest:
            noOfHighBreaks = noOfHighBreaks + 1
            highest = scores[n]
        if scores[n] < lowest:
            noOfLowBreaks = noOfLowBreaks + 1
            lowest = scores[n]
    return [noOfHighBreaks, noOfLowBreaks]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
