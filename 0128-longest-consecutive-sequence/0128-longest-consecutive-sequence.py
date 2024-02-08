class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        
        for num in nums:
            curr = num
            count = 0
            
            if curr - 1 not in seen:
                while curr in seen:
                    count+=1
                    curr+=1
            
                res = max(res, count)
        
        return res
                
                
                
            