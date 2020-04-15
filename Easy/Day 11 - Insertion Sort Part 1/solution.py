#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    # Pass last value out
    num = arr[-1]
    # Skip last index and loop backwards
    for i in range(len(arr)-2, -1, -1):
        # Fail condition: copy current index to the next
        if arr[i] > num:
            arr[i+1] = arr[i]
            print(" ".join(str(e) for e in arr))  
        # Success condition: copy the stored value to the next and stop the loop
        else:
            arr[i+1] = num
            print(" ".join(str(e) for e in arr))
            return

    #Handle testcase 2: smallest value at index 0
    arr[0] = num
    print(" ".join(str(e) for e in arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
