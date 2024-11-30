class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):
            mini = min (nums)
            
            for i in range (len(nums)):
                if mini == nums[i]:
                    nums[i] = nums[i] * multiplier
                    break
        
        return nums