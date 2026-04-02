#!/usr/bin/env python3
"""
********************************************************
    Author: Deepseek + CBOMBS
    Date:   March 26th, 2026

    HackerRank: Test two

    Input:
        Doctor's name
        Diagnosis ID (same ailment) (not data ID)

    Output:
        Minimum body temperature
        Maximum body temperature

    Sites: 
        https://jsonmock.hackerrank.com/api/medical_records

        https://jsonmock.hackerrank.com/api/medical_records?page=2


    TIME AND SPACE COMPLEXITY: Paginated API Filtering
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(N)       | N = total number of records across all pages.
                                    Each record is examined once for doctor name and diagnosis id.
                                    The number of HTTP requests equals total_pages, but total_pages ≤ N.
                                    
    Space Complexity | O(1)       | Only a fixed number of variables (page, min_temp, max_temp).
                                    Each page's JSON response is processed and discarded, so no cumulative storage.


*********************************************************
"""

import math
import os
import random
import re
import sys


import requests
import math

def bodyTemperature(doctorName, diagnosisId):
    url = "https://jsonmock.hackerrank.com/api/medical_records"
    
    page = 1
    min_temp = float('inf')
    max_temp = float('-inf')

    while True:
        response = requests.get(url, params={"page": page}).json()

        for record in response["data"]:
            if (
                record["doctor"]["name"] == doctorName and
                record["diagnosis"]["id"] == diagnosisId
            ):
                temp = record["vitals"]["bodyTemperature"]
                min_temp = min(min_temp, temp)
                max_temp = max(max_temp, temp)

        if page >= response["total_pages"]:
            break
        page += 1

    return [math.floor(min_temp), math.floor(max_temp)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    doctorName = input()

    diagnosisId = int(input().strip())

    result = bodyTemperature(doctorName, diagnosisId)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
