class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg_seen = set()
        pos_seen = set()
        res = -1
        
        for num in nums:
            if num > 0:
                pos_seen.add(num)
                
                if -num in neg_seen:
                    res = max(res, num)
            
            else:
                neg_seen.add(num)
                
                if -num in pos_seen:
                    res = max(res, -num)
                    
        return res