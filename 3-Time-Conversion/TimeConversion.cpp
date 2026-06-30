/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 28th, 2026
 *
 * HackerRank: #3 Time Conversion
 *
 * Given a time in 12-hour AM/PM format, convert it to
 * military time, also called 24-hour format.
 *
 * 12:00:00AM becomes 00:00:00.
 * 12:00:00PM stays    12:00:00.
 *
 *
 * Key Idea:
 *
 * The hour is always the first two characters.
 *
 * So:
 *
 * 1. Convert the first two characters into an integer hour.
 * 2. Read the AM/PM marker from the end of the string.
 * 3. If it is AM and the hour is 12, change the hour to 0.
 * 4. If it is PM and the hour is not 12, add 12.
 * 5. Replace the first two characters and return the first 8 chars.
 *
 *
 * Example:
 * s = "07:05:45PM"
 *
 * hour = 7
 * marker = PM
 *
 * Add 12.
 *
 * Return "19:05:45"
 *
 *
 * Constraints:
 *
 * s is a valid time in 12-hour AM/PM format.
 * s has the format hh:mm:ssAM or hh:mm:ssPM.
 *
 *
 * Compile and run:
 * g++ -std=c++23 TimeConversion.cpp -o TimeConversion && ./TimeConversion
 *
 * Solution:
 * Accepted
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Direct String Conversion
 * ------------------------------------------------------
 * Let:           s = input time string
 *
 * Time Complexity:  O(1)   | Fixed-size string operations
 * Space Complexity: O(1)   | Constant extra variables
 * ------------------------------------------------------
 *
 * ******************************************************
 */

#include <iostream>
#include <string>
#include <vector>
#include <unistd.h>

using namespace std;

/**
 * Converts 12-hour time format into 24-hour time format.
 *
 * @param s - input time string in hh:mm:ssAM/PM format
 * @return result - converted time string in HH:mm:ss format
 */
string timeConversion(const string& s)
{
    int h = stoi(s.substr(0, 2));
    char ap = s[8];

    // 12AM is the only AM hour that changes
    if (ap == 'A' && h == 12)
    {
        h = 0;
    }

    // PM hours after noon shift forward by 12
    if (ap == 'P' && h != 12)
    {
        h += 12;
    }

    string result = s.substr(0, 8);

    // Write the converted hour back into the answer
    result[0] = char('0' + h / 10);
    result[1] = char('0' + h % 10);

    return result;
}

/**
 * Runs local sample tests.
 *
 * @param none
 * @return void
 */
void runTests()
{
    // Test Case 1: HackerRank sample
    string test1 = "07:05:45PM";
    cout << "Input: " << test1 << endl;
    cout << "Output: "
         << timeConversion(test1)
         << endl;
    cout << "Expected: 19:05:45\n"
         << endl;

    // Test Case 2: Midnight edge case
    string test2 = "12:01:00AM";
    cout << "Input: " << test2 << endl;
    cout << "Output: "
         << timeConversion(test2)
         << endl;
    cout << "Expected: 00:01:00\n"
         << endl;

    // Test Case 3: Noon edge case
    string test3 = "12:01:00PM";
    cout << "Input: " << test3 << endl;
    cout << "Output: "
         << timeConversion(test3)
         << endl;
    cout << "Expected: 12:01:00\n"
         << endl;
}

int main()
{
    string s;

    // Local test path
    if (isatty(STDIN_FILENO))
    {
        runTests();
        return 0;
    }

    // HackerRank input path
    if (cin >> s)
    {
        cout << timeConversion(s) << endl;
        return 0;
    }

    // Fallback for no redirected input
    runTests();

    return 0;
}
