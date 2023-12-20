class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum, curr_sum = -float("inf"), 0
        l = 0
        
        for r in range(len(nums)):
            
            curr_sum+=nums[r]
            
            if r - l + 1 > k:
                curr_sum -= nums[l]
                l+=1
            if r-l+1 == k:   
                max_sum = max(max_sum, curr_sum)
            
        return max_sum / k
                
            
        