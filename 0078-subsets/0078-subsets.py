class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(i, subset):
            
            if i == n:
                res.append(subset.copy())
                return
            
            # for each, we can choose to take it or not to take it
            
            # take it
            backtrack(i+1, subset + [nums[i]])
            
            # dont take it
            backtrack(i+1, subset)
            
        backtrack(0, [])
        return res