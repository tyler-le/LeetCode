#include <algorithm>
#include <unordered_map>

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int i = 0;
        int max_so_far = INT_MIN;
        unordered_map<int,int> map;
        
        for (int j = 0; j < fruits.size(); j++) {
            map[fruits[j]]++;
            
            if (map.size() > 2) {
                map[fruits[i]]--;
                if (map[fruits[i]] == 0) map.erase(fruits[i]);
                i++;
            }
            
            max_so_far = max(max_so_far, j - i + 1);
        }
        
        return max_so_far;
    }
};