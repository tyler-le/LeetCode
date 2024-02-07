class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        # window size - take max freq
        
        hmap = defaultdict(int)
        l = 0
        n = len(nums)
        res = 0
        max_freq = 0
        
        for r in range(n):
            hmap[nums[r]]+=1
            max_freq = max(max_freq, hmap[nums[r]])
            
            while (r-l+1) - (max_freq) > k:
                hmap[nums[l]]-=1
                l+=1
            
            res = max(res, max_freq)
        
        return res
                      
                    