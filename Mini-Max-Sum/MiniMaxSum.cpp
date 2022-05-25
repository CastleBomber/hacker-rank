#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

string ltrim(const string&);
string rtrim(const string&);
vector<string> split(const string&);

// optimized for space
void miniMaxSum(vector<int> arr) {

    unsigned int sumMini = 0;
    unsigned int sumMax = 0;

    vector<int> sortedArray = arr;
    sort(sortedArray.begin(), sortedArray.end());

    for (int i = 0; i < arr.size() - 1; i++) {
        sumMini = sumMini + sortedArray[i];
    }

    sortedArray = arr;
    sort(sortedArray.begin(), sortedArray.end());
    //reverse(sortedArray.begin(), sortedArray.end()); // max values

    for (int i = 1; i < sortedArray.size(); i++) {
        sumMax = sumMax + sortedArray[i];
    }

    cout << sumMini << " ";
    cout << sumMax << endl;

}

int main()
{

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(5);

    for (int i = 0; i < 5; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    miniMaxSum(arr);

    return 0;
}

string ltrim(const string& str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string& str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string& str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
