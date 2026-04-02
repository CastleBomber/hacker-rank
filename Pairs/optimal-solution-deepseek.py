#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 25th, 2026

    HackerRank: Pairs 
    (better time, good space)

    Given an array of integers and a target value, 
    determine the number of pairs of array elements 
    that have a difference equal to the target value.

    Example:
        k = 1
        arr = [1, 2, 3, 4]
        
        There are three values that differ by k = 1: 2 - 1, 3 - 2, and 4 - 3. 
        Return 3.

    
    Function Description:
        Complete the pairs function below.
        pairs has the following parameter(s):
            int k: an integer, the target difference
            int arr[n]: an array of integers

    Returns:
        int: the number of pairs that satisfy the criterion

    Input Format:
        The first line contains two space-separated integers n and k, the size of arr and the target value.
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

    
    TIME AND SPACE COMPLEXITY: Set Membership Lookup
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Creating a set of n elements: O(n). 
                                    Then iterating through arr of size n: O(n) with O(1) average lookup.
                                    Overall O(2n) → O(n).
    Space Complexity | O(n)       | The set stores all n unique integers from arr.
                                    No other significant space usage.
*********************************************************
"""

import math
import os
import random
import re
import sys

def pairs(k, arr):
    '''
    Makes use of both the array and set
    '''
    s = set(arr)
    return sum(1 for x in arr if x + k in s)

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


