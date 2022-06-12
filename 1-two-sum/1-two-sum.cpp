#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> map;
        int complement;
        
        for (int i = 0; i < nums.size(); i++) {
            complement = target - nums[i];
            
            if (map.find(complement) != map.end()) return { i, map[complement] };
            map[nums[i]] = i;
        }
        
        return {};
    }
};