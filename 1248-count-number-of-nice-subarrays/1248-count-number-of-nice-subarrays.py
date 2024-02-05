class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # number of subarrays with at most k odds
        
        def at_most(k):
            if k < 0: return 0
            
            l = 0
            num_odds = 0
            res = 0
            
            for r in range(len(nums)):
                num_odds += (1 if nums[r] % 2 else 0)
                
                while num_odds > k:
                    num_odds -= (1 if nums[l] % 2 else 0)
                    l+=1
                
                res += (r-l+1)
                
            return res
                
            
        
        return at_most(k) - at_most(k-1)