#!/usr/bin/env python3
"""
********************************************************
    Author: Deepseek + CBOMBS
    Date:   March 26th, 2026

    HackerRank: Test #1
    Position:   IBM Software Engineer Apprentice

    Calculates the maximum number of non-overlapping time windows that can be selected

    Notes: 
        Activity Selection Problem — pick the maximum number of non-overlapping intervals
        

    TIME AND SPACE COMPLEXITY: Greedy Interval Scheduling
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n log n) | Sorting the n intervals by end time dominates.
                                    The subsequent linear scan is O(n).

    Space Complexity | O(n)       | The `intervals` list stores n tuples (start, end).
                                    Input arrays are already O(n), but this algorithm creates an explicit list of pairs.

*********************************************************
"""

import math
import os
import random
import re
import sys


def selectMostCompatibleWindows(startTime, endTime):
    # pair and sort by end time
    intervals = sorted(zip(startTime, endTime), key=lambda x: x[1])

    count = 0
    last_end = -1

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # startTime_count = int(input().strip())

    # startTime = []

    # for _ in range(startTime_count):
    #     startTime_item = int(input().strip())
    #     startTime.append(startTime_item)

    # endTime_count = int(input().strip())

    # endTime = []

    # for _ in range(endTime_count):
    #     endTime_item = int(input().strip())
    #     endTime.append(endTime_item)


    n = 3
    startTime = [1,1,2]
    endTime = [3,2,4] 
    result = selectMostCompatibleWindows(startTime, endTime)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()