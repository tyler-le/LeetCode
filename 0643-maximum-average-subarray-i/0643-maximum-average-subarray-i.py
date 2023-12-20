class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        curr_sum = 0
        
        for r in range(k):
            curr_sum+=nums[r]
        
        max_sum = curr_sum
        
        for r in range(k, len(nums)):
            curr_sum+=nums[r]
            curr_sum-=nums[l]
            l+=1
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k
                
            
        