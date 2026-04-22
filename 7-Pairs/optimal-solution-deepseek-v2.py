#!/usr/bin/env python3
"""
********************************************************
    Author: Deepseek + CBOMBS
    Date:   March 25th, 2026

    HackerRank: Pairs 
    (longer time, better space)

    Given an array of integers and a target value, 
    determine the number of pairs of array elements 
    that have a difference equal to the target value.

    Example:
        k = 1
        arr = [1, 2, 3, 4]
        
        There are three values that differ by k = 1: 2 - 1, 3 - 2, and 4 - 3. Return 3.

    
    Function Description:
        Complete the pairs function below.
        pairs has the following parameter(s):
            int k: an integer, the target difference
            int arr[n]: an array of integers

    Returns:
        int: the number of pairs that satisfy the criterion

    Input Format:
        The first line contains two space-separated integers n and k, 
        the size of arr and the target value.
        The second line contains n space-separated integers of the array arr.

    Constraints:
        2 ≤ n ≤ 10^5
        0 ≤ k ≤ 10^9
        0 ≤ arr[i] ≤ 2^31 - 1
        each integer arr[i] will be unique

    Sample Input:
        STDIN       Function
        -----       --------
        5 2         arr[] size n = 5, k = 2
        1 5 3 4 2   arr = [1, 5, 3, 4, 2]

    Sample Output:
        3

    Explanation:
        There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1].

    Usage:
        python3 main.py

    Solution:
    

    Notes:
        Test prep for IBM Software Engineer Apprentice

    TIME AND SPACE COMPLEXITY: Two‑Pointer with Sorting
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n log n) | Sorting the array takes O(n log n) comparisons.
                                    The subsequent linear scan runs in O(n) (each pointer moves at most n steps).
                                    Overall dominated by sorting.
    Space Complexity | O(1)       | Excluding the input array, only a few integer variables (i, j, count) are used.
                                    Sorting (Timesort) may use O(n) temporary space, but algorithm itself is O(1).    

*********************************************************
"""

import math
import os
import random
import re
import sys

def pairs(k, arr):
    arr.sort()
    count = 0
    i = 0
    for j in range(len(arr)):
        while i < j and arr[j] - arr[i] > k:
            i += 1
        if arr[j] - arr[i] == k:
            count += 1

    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # arr = list(map(int, input().rstrip().split()))

    k = 2
    arr = [1, 5, 3, 4, 2]
    result = pairs(k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()





