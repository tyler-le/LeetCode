class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        res = 0
        
        while k:
            res+=mx
            mx+=1
            k-=1
        
        return res