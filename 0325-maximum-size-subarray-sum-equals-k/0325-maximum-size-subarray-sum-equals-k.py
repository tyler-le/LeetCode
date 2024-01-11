class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hmap = defaultdict(int)
        hmap[0] = -1
        
        # map prefix sum to where that prefix sum occurs
        curr_sum = 0
        total_sum = sum(nums)
        res = 0
        
        for i, num in enumerate(nums):
            curr_sum+=num
            
            if curr_sum - k in hmap:
                res = max(res, i - hmap[curr_sum-k])
            
            if curr_sum not in hmap:
                hmap[curr_sum] = i
            
        return res
       
    