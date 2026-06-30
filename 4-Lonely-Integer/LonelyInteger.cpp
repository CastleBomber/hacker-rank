/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 28th, 2026
 *
 * HackerRank: #4 Lonely Integer
 *
 * Given an array of integers, where all elements but one
 * occur twice, find the unique element.
 *
 *
 * Key Idea:
 *
 * Use XOR.
 *
 * XOR has two useful properties:
 *
 * x ^ x = 0
 * x ^ 0 = x
 *
 * So every duplicate pair cancels itself out.
 * The only number left is the lonely integer.
 *
 *
 * Example:
 * a = [1, 2, 3, 4, 3, 2, 1]
 *
 * 1 ^ 2 ^ 3 ^ 4 ^ 3 ^ 2 ^ 1
 *
 * Duplicate values cancel.
 *
 * Return 4
 *
 *
 * Constraints:
 *
 * 1 <= n < 100
 * n is odd
 * 0 <= a[i] <= 100
 * All elements except one occur twice.
 *
 *
 * Compile and run:
 * g++ -std=c++23 LonelyInteger.cpp -o LonelyInteger && ./LonelyInteger
 *
 * Solution:
 * Accepted
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: XOR Scan
 * ------------------------------------------------------
 * Let:           n = a.size()
 *
 * Time Complexity:  O(n)   | Scan each number once
 * Space Complexity: O(1)   | Constant extra variables
 * ------------------------------------------------------
 *
 * ******************************************************
 */

#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;

/**
 * Finds the only value that does not have a duplicate.
 *
 * @param a - input vector where every value except one appears twice
 * @return result - value that appears once
 */
int lonelyinteger(const vector<int>& a)
{
    int result = 0;

    // Duplicate values cancel out with XOR
    for (int x : a)
    {
        result ^= x;
    }

    return result;
}

/**
 * Prints a vector in readable C++ format.
 *
 * @param nums - input vector of integers
 * @return void
 */
void printVector(const vector<int>& nums)
{
    cout << "{";

    for (size_t i = 0; i < nums.size(); i++)
    {
        cout << nums[i];

        if (i < nums.size() - 1)
        {
            cout << ", ";
        }
    }

    cout << "}";
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
    vector<int> test1 = {1, 2, 3, 4, 3, 2, 1};
    cout << "Input: ";
    printVector(test1);
    cout << endl;
    cout << "Output: "
         << lonelyinteger(test1)
         << endl;
    cout << "Expected: 4\n"
         << endl;

    // Test Case 2: Single element edge case
    vector<int> test2 = {1};
    cout << "Input: ";
    printVector(test2);
    cout << endl;
    cout << "Output: "
         << lonelyinteger(test2)
         << endl;
    cout << "Expected: 1\n"
         << endl;

    // Test Case 3: Lonely value in the middle
    vector<int> test3 = {0, 0, 5, 9, 9};
    cout << "Input: ";
    printVector(test3);
    cout << endl;
    cout << "Output: "
         << lonelyinteger(test3)
         << endl;
    cout << "Expected: 5\n"
         << endl;
}

int main()
{
    int n;

    // Local test path
    if (isatty(STDIN_FILENO))
    {
        runTests();
        return 0;
    }

    // HackerRank input path
    if (cin >> n)
    {
        vector<int> a(n);

        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        cout << lonelyinteger(a) << endl;
        return 0;
    }

    // Fallback for no redirected input
    runTests();

    return 0;
}
