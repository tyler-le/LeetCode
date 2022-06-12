#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        vector<int> res;
        int complement;
        
        for (int i = 0; i < nums.size(); i++) {
            complement = target - nums[i];
            
            if (map.find(complement) != map.end()) {
                res = { i, map[complement] };
                return res;
            }
            
            map[nums[i]] = i;
        }
        
        return res;
    }
};