#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <string>


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        
        int max_so_far = INT_MIN;
        int count = 0;
        int begin = 0;
        int end = 0;
        int row = 0;
        const int S_LEN = s.length();
    
        
        while(end < S_LEN) {
            if (map.find(s[end]) == map.end() || map.find(s[end])->second == 0) {
                map[s[end]]++;
                end++;
                count++;
            }
            
            else {
                max_so_far = std::max(count, max_so_far);
                map[s[begin]] = 0;
                begin++;
                count--;

            }
        }
        
        return count > max_so_far ? count : max_so_far;
    }
};