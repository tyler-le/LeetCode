class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        l = 0
        n = len(nums)
        
        hmap = defaultdict(int)
        
        # keep track of min/max in window
        # contract window when max - min > limit
        # to (re)set the max/min values, we can use a min heap and max heap for the window
        
        for r in range(n):
            
            
            hmap[nums[r]]+=1
            
            while max(hmap.keys()) - min(hmap.keys()) > limit:
                
                hmap[nums[l]]-=1
                if not hmap[nums[l]]: del hmap[nums[l]]
                l+=1
            
            res = max(res, r-l+1)
        
        return res