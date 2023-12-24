class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # map prefix_sum : earliest index
        hmap = {}
        hmap[0] = -1
        prefix_sum = 0
        res = 0
        
        for i, num in enumerate(nums):
            prefix_sum+=num
            
            if prefix_sum - k in hmap:
                res = max(res, i - (hmap[prefix_sum - k]))
            
            if prefix_sum not in hmap:
                hmap[prefix_sum] = i
                
        return res
            