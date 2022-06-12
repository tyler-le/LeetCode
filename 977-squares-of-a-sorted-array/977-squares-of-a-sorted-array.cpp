class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> squared;
        for (auto& num : nums) {
            squared.push_back(num*num);
        }
        
        std::sort(squared.begin(), squared.end());
        
        return squared;
    }
};