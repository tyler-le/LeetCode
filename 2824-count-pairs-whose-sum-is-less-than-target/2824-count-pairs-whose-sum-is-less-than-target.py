class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        
#         curr = -1
#         right_index = 3
#         i = 0
        
#         -1, 1, 1, 2, 3
        
        n = len(nums)
        nums.sort()
        right = n - 1
        res = 0
        
        for i in range(n):
            curr = nums[i]
            
            while i < right and curr + nums[right] >= target:
                right -= 1
                
            if curr + nums[right] < target:
                res+=(right - i)
        
        return res
            
            
                
            