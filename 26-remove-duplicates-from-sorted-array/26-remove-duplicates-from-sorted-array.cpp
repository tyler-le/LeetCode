class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // two pointer approach
        // one to keep insertion location, the other to find next non-duplicate to insert
        int l = 0;
        int r = 0;
        int size = nums.size();
        
        while (r < size) {
            while (r < size && nums[r] == nums[l]) r++;
            l++;
            if (r < size) nums[l] = nums[r];
        }
        
        return l;
    }
};