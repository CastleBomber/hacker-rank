#!/usr/bin/env python3
"""
********************************************************
    Author: ChatGPT + CBOMBS
    Date:   April 16th, 2026

    HackerRank: Test #1 
    Position:   IBM Maximo Developer


    Problem:
        Compute sum of XOR for all pairs (a, b)
        where a ∈ arr1 and b ∈ arr2.

    ----------------------------------------------------
    Time & Space Complexity
    ----------------------------------------------------
    Approach: Bitwise Counting (Greedy per bit)

    Let:
        n = len(arr1)
        m = len(arr2)

    Time Complexity:
        O(32 * (n + m)) ≈ O(n + m)
        - We iterate over 32 bits
        - For each bit, scan both arrays once

    Space Complexity:
        O(1)
        - No extra data structures (constant space)

    ----------------------------------------------------
    Key Insight:
        XOR = 1 when bits are DIFFERENT

        Instead of checking all pairs (O(n*m)),
        we count how many pairs produce a 1 at each bit.
*********************************************************
"""

from typing import List

def maximumXorSum(arr1: List[int], arr2: List[int]) -> int:
    MOD = 10**9 + 7
    result = 0

    # Iterate through each bit position (0 to 31)
    for bit in range(32):
        mask = 1 << bit  # isolate current bit (e.g., 1, 2, 4, 8, ...)

        # Count how many numbers in arr1 have this bit = 1
        countA_1 = sum(1 for a in arr1 if a & mask)
        countA_0 = len(arr1) - countA_1  # remaining have bit = 0

        # Same for arr2
        countB_1 = sum(1 for b in arr2 if b & mask)
        countB_0 = len(arr2) - countB_1

        # XOR produces 1 when bits are different:
        # (1 from A with 0 from B) OR (0 from A with 1 from B)
        pairs = (countA_1 * countB_0) + (countA_0 * countB_1)

        # Each such pair contributes (2^bit) to total sum
        contribution = pairs * mask

        # Add contribution to result (modulo to prevent overflow)
        result = (result + contribution) % MOD

    return result


if __name__ == '__main__':
    # Example test
    arr1 = [1, 2, 3]
    arr2 = [10, 10, 10]

    result = maximumXorSum(arr1, arr2)
    print(result)