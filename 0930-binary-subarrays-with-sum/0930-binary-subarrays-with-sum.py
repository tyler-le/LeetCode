class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # subarrays that have sum <= k, using sliding window
        def at_most(k):
            if k < 0: return 0           
            l, res, curr_sum, n = 0, 0, 0, len(nums)
            
            for r in range(n):
                curr_sum += nums[r]
                    
                while curr_sum > k:
                    curr_sum-=nums[l]
                    l+=1
                    
                res+=(r-l+1) # number of subarrays ending at nums[r]
                    
            return res
                
        # (num subarrays with sum <= k) - (num subarrays with sum <= k-1) = (num subarrays with sum k)
        return at_most(goal) - at_most(goal-1)
            