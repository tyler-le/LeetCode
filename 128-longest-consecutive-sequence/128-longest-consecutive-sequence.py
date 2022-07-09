class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        max_len = 0
        
        for num in nums:
            # check if the start of a sequence
            if num-1 in nums:
                continue
            
            
            start = num
            seq_len = 0
            while start in nums:
                seq_len += 1
                start += 1
            max_len = max(max_len, seq_len)
            
        return max_len
                    
                    
                