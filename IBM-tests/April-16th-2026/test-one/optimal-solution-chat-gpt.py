#!/usr/bin/env python3
"""
********************************************************
    Author: ChatGPT + CBOMBS
    Date:   April 16th, 2026

    HackerRank: Test #1



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
    MOD = 10**9 + 7
    result = 0

    for bit in range(32):  # 32 bits for integers
        mask = 1 << bit

        countA_1 = sum(1 for a in arr1 if a & mask)
        countA_0 = len(arr1) - countA_1

        countB_1 = sum(1 for b in arr2 if b & mask)
        countB_0 = len(arr2) - countB_1

        # XOR = 1 when bits differ
        pairs = countA_1 * countB_0 + countA_0 * countB_1

        result += pairs * mask
        result %= MOD

    return result


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
  
