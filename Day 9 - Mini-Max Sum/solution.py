#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min = sum(arr) - arr[0]
    max = sum(arr) - arr[0]
    for n in range(0,len(arr)):
        if (sum(arr) - arr[n]) > max:
            max = sum(arr) - arr[n]
        if min > (sum(arr) - arr[n]): 
            min = sum(arr) - arr[n]
    print(min, max)

    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print ( sum-max(arr), sum-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
