#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   April 16th, 2026

    HackerRank: Test #2



*********************************************************
"""

from typing import Optional, List, Dict, Tuple, Set
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify
import math
import bisect
import itertools
import functools
import os
import random
import re
import sys
import requests

def findMinimumLengthSubarray(arr, k):
    distinct = set()
    distinctCount = 0
    lengthCount = 0
    saved = {}

    for n in range(len(arr)):
        if arr[n] not in distinct:
            distinct.add(arr[n])
            distinctCount += 1
            lengthCount += 1
        else: 
            while arr[n] in distinct:
                lengthCount += 1
        
        saved.add(distinctCount, lengthCount)

    smallest = int('inf')

    for x in saved:
        if saved[x][1] >= k and saved[x][1] < smallest:
            smallest = 0
        

    return smallest
        


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    # arr = []

    # for _ in range(arr_count):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    # k = int(input().strip())

    arr = [3, 2, 3, 3, 1, 3]
    k = 3
    result = findMinimumLengthSubarray(arr, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
