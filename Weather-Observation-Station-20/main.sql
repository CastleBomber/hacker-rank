"""
********************************************************
    Author: DeepSeek + CBOMBS
    Date:   March 24th, 2026

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

        Uses standard SQL (ISO/ANSI) with window functions (ROW_NUMBER, COUNT(*) OVER). 
    It works on:
        SQL Server
        PostgreSQL
        MySQL 8.0+
        Oracle (also supports it)
        DB2
        SQLite (with window functions enabled)

*********************************************************
"""

SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
           COUNT(*) OVER () AS total
    FROM STATION
) t
WHERE row_num IN (FLOOR((total + 1) / 2), CEIL((total + 1) / 2));