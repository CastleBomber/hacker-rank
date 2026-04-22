/*
    Author: CBOMBS
    Date: May 29th, 2022

    HackerRank: Time Conversion
*/
#include <bits/stdc++.h>
#include <string.h>
#include <iostream>

using namespace std;

/*
    Given time in AM/PM format, convert it to MILITARTY TIME

    String s -
    Ex:
    STD                     MILITARTY
    '12:03:00AM'    returns '00:03:00'
    '12:03:00PM'    returns '12:03:00'
    '07:05:45PM'    returns '19:05:45'
 */

string timeConversion(string s) {

  int hours;
  string militaryTime;
  string tmp;

  tmp = s.substr(0, 2);
  tmp.erase(0, min(tmp.find_first_not_of('0'), tmp.size()-1)); // erases leading zero; handles sp case all 0
  hours = stoi(tmp);

  if(s.find("AM") != string::npos){ // AM found

    if(s.substr(0,2).find("12") != string::npos){ // handles special case 12AM -> 00AM
      militaryTime = "00" + s.substr(2,6);
    } else {
        militaryTime = s.substr(0, 8);
    }

  } else if (s.find("PM") != string::npos) { // PM found

      if(!(s.substr(0,2).find("12") != string::npos)) { // STD 12PM not found
          hours = hours + 12;
      }

      militaryTime = to_string(hours) + s.substr(2, 6); // combines '12' ':00:00'

  }

  return militaryTime;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
