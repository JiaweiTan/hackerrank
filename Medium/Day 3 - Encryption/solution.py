#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    import math 
    # Remove spaces
    s.strip()
    col = math.ceil(math.sqrt(len(s)))
    row = math.floor(math.sqrt(len(s)))
        
    if (row * col) < len(s):
        row = col

    val = ''
    for i in range(col):
        val += s[i : len(s) : col] + " "
        
    return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
