class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        
        /**
        * This naive approach is O(nlogn)
        **/
        vector<int> squared;
        for (auto& num : nums) {
            squared.push_back(num*num);
        }
        
        std::sort(squared.begin(), squared.end());
        
        return squared;
        
        /**
        * This approach is O(n)
        **/
        
        // Should use absolute value somewhere.
        
    }
};