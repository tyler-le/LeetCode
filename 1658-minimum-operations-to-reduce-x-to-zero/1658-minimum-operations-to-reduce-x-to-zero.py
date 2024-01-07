class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # sliding window of n - x - 1
        
        
        
#         sum(nums) - x
        
#         prefix sum
        
#         find max subarray that equals sum(nums) - x
        
        
        sumi = sum(nums)
        curr_sum = 0
        l = 0
        target = sumi - x
        res = -1
        if not target: return len(nums)
        for r in range(len(nums)):
            curr_sum+=nums[r]
            
            while l < len(nums) and curr_sum > target:
                curr_sum-=nums[l]
                l+=1
            
            if l < len(nums) and curr_sum == target:
                res = max(res, r-l+1)
                
                
        return len(nums) - res if res!=-1 else res
            
        