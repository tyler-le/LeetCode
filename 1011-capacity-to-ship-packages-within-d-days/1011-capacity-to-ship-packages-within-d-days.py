class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        l, r = max(weights), sum(weights)
        
        def satisfies(capacity):
            count = 1
            curr = 0
            
            for weight in weights:
                if curr + weight > capacity:
                    count+=1
                    curr = 0
                curr+=weight
            
            return count <= days
                
                
        
        while l < r:
            mid = (r + l) // 2
            if satisfies(mid):
                r = mid
            else:
                l = mid+1
                
        return l
                