#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

def hourglassSum(arr):
    maxsum=-90
    
    for i in range(4):
        for j in range(4):
            top=sum(arr[i][j:j+3])
            mid=arr[i+1][j+1]
            bot=sum(arr[i+2][j:j+3])
            
            hourglass=top+mid+bot
            
            maxsum=max(hourglass,maxsum)
    return maxsum
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
