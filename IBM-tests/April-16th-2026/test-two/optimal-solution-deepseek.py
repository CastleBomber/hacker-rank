#!/usr/bin/env python3
"""
********************************************************
    Author: DeepSeek + ChatGPT CBOMBS
    Date:   April 16th, 2026

    HackerRank: Test #2
    Position:   IBM Maximo Developer

    Problem:
        Find the minimum length subarray that contains
        at least k DISTINCT integers.

    ----------------------------------------------------
    Time & Space Complexity
    ----------------------------------------------------
    Approach: Sliding Window + Hash Map

    Let:
        n = len(arr)

    Time Complexity:
        O(n)
        - Each element is processed at most twice:
          once by right pointer, once by left pointer

    Space Complexity:
        O(k) → worst case O(n)
        - Hash map stores frequency of elements in window

    ----------------------------------------------------
    Key Insight:
        - Use a sliding window [left → right]
        - Expand right to gain distinct elements
        - Shrink left to minimize window once condition met

    Goal:
        Maintain smallest window where distinct >= k
*********************************************************
"""

from typing import List

def findMinimumLengthSubarray(arr: List[int], k: int) -> int:
    n = len(arr)

    # If total unique elements in array < k → impossible
    if k > len(set(arr)):
        return -1

    # If we only need 1 distinct → any single element works
    if k == 1:
        return 1

    freq = {}          # stores frequency of elements in current window
    left = 0           # left pointer of window
    distinct = 0       # number of distinct elements in window
    min_len = float('inf')

    # Expand window with right pointer
    for right in range(n):
        val = arr[right]

        # Add current element to frequency map
        freq[val] = freq.get(val, 0) + 1

        # If this is the first occurrence → new distinct element
        if freq[val] == 1:
            distinct += 1

        # Try shrinking window while condition is satisfied
        # (we want smallest valid window)
        while distinct >= k:
            # Update minimum length
            min_len = min(min_len, right - left + 1)

            # Remove leftmost element from window
            left_val = arr[left]
            freq[left_val] -= 1

            # If frequency drops to 0 → we lost a distinct element
            if freq[left_val] == 0:
                distinct -= 1

            # Move left pointer to shrink window
            left += 1

    # If no valid window found, return -1
    return min_len if min_len != float('inf') else -1


if __name__ == '__main__':
    arr = [3, 2, 3, 3, 1, 3]
    k = 3

    result = findMinimumLengthSubarray(arr, k)
    print(result)