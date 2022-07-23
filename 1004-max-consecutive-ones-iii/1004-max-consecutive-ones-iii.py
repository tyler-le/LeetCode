class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        
        # map bit to frequency
        count = [0,0]
        
        l = 0
        
        for r in range (len(nums)):
            count[nums[r]] += 1
            
            num_replacements = (r-l+1) - count[1]
            while num_replacements > k:
                count[nums[l]] -= 1
                l+=1
                num_replacements = (r-l+1) - count[1]    
            res = max(res, r-l+1)
            
        return res