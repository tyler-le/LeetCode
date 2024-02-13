class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        n = len(nums)
        
        for r in range(n):
            
            if not nums[r]:
                while nums[l]:
                    l+=1
                res+=(r-l+1)
            else:
                l = r
            
        return res
            
            
        