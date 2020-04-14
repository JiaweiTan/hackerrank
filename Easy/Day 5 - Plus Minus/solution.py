#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0;
    for n in range(0, length):
        if arr[n] == 0:
            zero += 1
        elif arr[n] > 0:
            positive += 1
        else:
            negative += 1 
    print("{:.6f}".format(positive/length))
    print("{:.6f}".format(negative/length))
    print("{:.6f}".format(zero/length)) 


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
