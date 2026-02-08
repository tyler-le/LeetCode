class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        total = 0

        for i in range(n-1, 0, -1):
            total+=nums[i]
            if nums[i-1] > (total / (n - i)):
                res+=1            
             
        return res