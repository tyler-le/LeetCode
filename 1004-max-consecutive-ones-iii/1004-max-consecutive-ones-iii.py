class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = 0
        res = 0
        l = 0
        
        for r in range(len(nums)):
            if not nums[r]:
                flipped+=1
            
            while flipped > k:
                if not nums[l]:
                    flipped-=1
                l+=1
                
            res = max(res, r-l+1)
        
        return res