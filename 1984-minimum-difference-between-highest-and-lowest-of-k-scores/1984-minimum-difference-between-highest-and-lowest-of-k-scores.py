class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sort and sliding window of k
        nums.sort()
        res = float("inf")
        
        for i in range(len(nums) - k + 1):
            res = min(res, abs(nums[i] - nums[i+k-1]))  
        
        return res
            
                
            