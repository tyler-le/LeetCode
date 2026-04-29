class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def at_most(x):
            # returns the number of subarrays with at most x odds
            l, n = 0, len(nums)
            num_odds = 0
            res = 0

            for r in range(n):
                if nums[r] % 2:
                    num_odds+=1

                while num_odds > x:
                    if nums[l] % 2:
                        num_odds-=1
                    l+=1
                
                if num_odds <= x:
                    res+=(r-l+1)

            return res
        return at_most(k) - at_most(k-1)