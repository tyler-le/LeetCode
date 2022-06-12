#include <unordered_map>
#include <algorithm>


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        
        int max_so_far = INT_MIN;
        int count = 0, begin = 0, end = 0, row = 0;
        const int S_LEN = s.length();
    
        
        while(end < S_LEN) {
            auto mapping = map.find(s[end]);
            
            // if char not in map or its value is 0, increment char in map and slide the                end of window to the right
            if (mapping == map.end() || mapping->second == 0) {
                map[s[end]]++;
                end++;
                count++;
            }
            
            // if dupl char found, delete char at position 'begin' and slide start of                    window over by 1 and decrement count
            // then check for new max
            else {
                max_so_far = std::max(count, max_so_far);
                map[s[begin]]--;
                begin++;
                count--;

            }
        }
        
        return count > max_so_far ? count : max_so_far;
    }
};