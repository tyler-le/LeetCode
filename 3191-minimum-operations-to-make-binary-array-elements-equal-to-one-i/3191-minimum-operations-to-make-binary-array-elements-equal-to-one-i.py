class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # simulate and greedily flip 0
        n = len(nums)
        res = 0

        for i in range(n-2):

            if nums[i] == 0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                res+=1
        
        
        if n != sum(nums): return -1
        return res
