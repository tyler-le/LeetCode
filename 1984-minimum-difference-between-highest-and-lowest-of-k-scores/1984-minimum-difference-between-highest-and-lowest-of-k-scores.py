class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - k + 1):
        
            diff = abs(nums[i] - nums[i+k-1])
            res = min(res, diff)
            
        return res if res != float('inf') else 0