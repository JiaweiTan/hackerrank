#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def isKaprekar(n):
    s = str(n*n)
    right = s[len(s)//2:]
    if s[:len(s)//2] == '':
        left = '0'  
    else:
        left = s[:len(s)//2]
    if int(left) + int(right) == n:
        return True  
    else:
        False

def kaprekarNumbers(p, q):
    output = []
    for num in range(p, q + 1):
        if isKaprekar(num) == True:
            output.append(num)
    if len(output) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(x) for x in output))           


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
