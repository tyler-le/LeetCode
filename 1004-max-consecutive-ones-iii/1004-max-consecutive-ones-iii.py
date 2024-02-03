class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        res = 0
        l = 0
        num_flipped = 0
        
        for r in range(len(nums)):
            if not nums[r]:
                num_flipped+=1
                
            while num_flipped > k:
                if nums[l] == 0:
                    num_flipped-=1
                l+=1
            
            res = max(res, r-l+1)
 
        return res