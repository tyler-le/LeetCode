class Solution:
    def thirdMax(self, nums: List[int]) -> int:
                
        nums = list(set([-num for num in nums]))
        
        heapify(nums)
        
        if len(nums) < 3: return -nums[0]
        
        for i in range(2):
            heappop(nums)
        
        return -nums[0]
        