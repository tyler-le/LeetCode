#include <stdlib.h>     /* abs */
#include <vector>

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        /**
        * This naive approach is O(nlogn) due to sorting
        **/
//         vector<int> squared;
//         for (auto& num : nums) {
//             squared.push_back(num*num);
//         }
        
//         std::sort(squared.begin(), squared.end());
        
//         return squared;
        
        /**
        * This approach is O(n)
        **/
        
        vector<int> squared;
        int l = 0;
        int r = nums.size() - 1;
        
        if (nums.size() == 0) return squared;
        
        while (l < r) {
            if (abs(nums[l]) > abs(nums[r])) {
                squared.insert(squared.begin(), nums[l] * nums[l]); // vector has no 'push_front' 
                l++;
            }
            
            else if (abs(nums[l]) <= abs(nums[r])) {
                squared.insert(squared.begin(), nums[r] * nums[r]);
                r--;
            }
            
        }

        squared.insert(squared.begin(), nums[l] * nums[l]);
        
        return squared;
    }
};