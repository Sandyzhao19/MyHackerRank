#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMaxValue(arr):
    # Write your code here
    arr.sort()
    
    curr_value = 1
    
    for num in arr[1:]:
        if num - curr_value > 1:
            num = curr_value + 1
        curr_value = num
    
    return curr_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMaxValue(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
