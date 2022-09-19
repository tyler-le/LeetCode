class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hmap;
        
        
        for(int i = 0; i < nums.size(); i++){
            auto complement = target - nums[i];
            if (hmap.find(complement) == hmap.end()){
                hmap[nums[i]] = i;
            }
            else {
                return {i, hmap[complement]};
            }
            
        }
        return {};
    }
};