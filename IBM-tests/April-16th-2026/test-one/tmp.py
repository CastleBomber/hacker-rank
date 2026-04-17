#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   April 16th, 2026

    HackerRank: Test #1

    Solution:
        Solved
        But too time intensive

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

def maximumXorSum(arr1, arr2):
    A = arr1
    B = arr2

    matrix = [[a ^ b for b in B] for a in A]
    total = sum(sum(row) for row in matrix)


    answer = total % ((10**9) + 7)

    

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr1_count = int(input().strip())

    # arr1 = []

    # for _ in range(arr1_count):
    #     arr1_item = int(input().strip())
    #     arr1.append(arr1_item)

    # arr2_count = int(input().strip())

    # arr2 = []

    # for _ in range(arr2_count):
    #     arr2_item = int(input().strip())
    #     arr2.append(arr2_item)


    arr1 = [1, 2, 3]
    arr2 = [10, 10, 10]

    result = maximumXorSum(arr1, arr2)

    # fptr.write(str(result) + '\n')

    # fptr.close()
  
