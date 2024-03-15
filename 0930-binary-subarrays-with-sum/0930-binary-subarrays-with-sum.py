class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # number of nonempty subarrays with AT MOST 'k' ones
        def at_most(k):
            if k < 0: return 0
            
            num_ones = 0
            l = 0
            n = len(nums)
            res = 0
            
            for r in range(n):
                num_ones+=nums[r]
                
                while num_ones > k:
                    num_ones-=nums[l]
                    l+=1
                
                res+=(r-l+1)
            
            return res
            
        return at_most(goal) - at_most(goal - 1)