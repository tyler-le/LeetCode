
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        /**
        * This approach is O(n)
        **/
        
        // two pointer
        // one at front, one at end. we will take the abs. value of each and push the one with the bigger                square to the end of the resulting array and adjust pointers when needed.
        vector<int> squared(nums.size(), -1);
        
        // we use curr to insert because there is no 'push_front' and using iterators is too slow
        int curr = nums.size() - 1;
        
        int l = 0;
        int r = nums.size() - 1;
        
        if (nums.size() == 0) return squared;
        
        while (l < r) {
            
            // if left has bigger abs. value, we push its square to result
            if (abs(nums[l]) > abs(nums[r])) {
                squared[curr] = nums[l] * nums[l];
                curr--;
                l++;
            }
            
            // if right has bigger (or equal) abs, we push its square to result
            else if (abs(nums[l]) <= abs(nums[r])) {
                squared[curr] = nums[r] * nums[r];
                curr--;
                r--;
            }
            
        }

        // when l == r (aka size of nums is 1)
        // also the while-loop does not handle this case, so we do it here
        squared[curr] = nums[l] * nums[l];
        curr--;
        
        return squared;
    }
};