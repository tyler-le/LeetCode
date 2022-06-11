#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map;

        // if lengths are not same, can't be anagram
        if (s.length() != t.length()) return false;
        
        // loop through s and populate map
        for (auto c : s) {
            if (s_map.find(c) == s_map.end()) s_map[c] = 1;
            else s_map[c]++;
        }
        
        // loop through t and decrement from s_map for every char in t 
        for (auto c : t) {
            if (s_map.find(c) == s_map.end() || s_map[c] == 0) return false;
            else s_map[c]--;
        }
        
        // loop through s_map, should all be zero if valid anagram
        for (auto itr = s_map.begin(); itr != s_map.end(); itr++) {
            if (itr->second != 0) return false;
        }
        
        return true; 
    }
};