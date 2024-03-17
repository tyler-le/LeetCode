class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sums = {}
        prefix_sums[0] = -1
        acc = 0
        res = 0
        
        for i in range(len(nums)):
            num = nums[i]
            acc+=num
            
            if acc - k in prefix_sums:
                res = max(res, i - prefix_sums[acc - k])
                
            if acc not in prefix_sums:
                prefix_sums[acc] = i
                
        return res
                
            
            
            
            
            