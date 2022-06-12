class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // two pointer approach
        int l = 0;
        int r = 0;
        
        if (nums.size() == 1) return 1;
        
        while (r < nums.size()) {
            while (r < nums.size() && nums[r] == nums[l]) r++;
            
            l++;
            
            if (r < nums.size()) nums[l] = nums[r];
        }
        
        return l;
    }
};