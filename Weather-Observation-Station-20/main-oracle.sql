"""
********************************************************
    Author: DeepSeek + CBOMBS
    Date:   March 25th, 2026

    HackerRank: Weather Observation Station 20

    A median is defined as a number separating the higher half of a data set from the lower half. 
    Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

    Input Format
    The STATION table is described as follows:

    STATION

    +---------+-------------+-------------+
    | Field   | Type        | Description |
    +---------+-------------+-------------+
    | ID      | NUMBER      | Station ID  |
    | CITY    | VARCHAR2    | City name   |
    | STATE   | VARCHAR2    | State name  |
    | LAT_N   | NUMBER      | Northern latitude |
    | LONG_W  | NUMBER      | Western longitude |
    +---------+-------------+-------------+

    where LAT_N is the northern latitude and LONG_W is the western longitude.

    

    Notes:
        Test prep for IBM Software Engineer Apprentice

        Oracle‑specific
        Not part of the standard SQL and will not run on most other databases
        
*********************************************************
"""

SELECT ROUND(MEDIAN(LAT_N), 4) FROM STATION;