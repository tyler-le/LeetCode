class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        hmap = collections.defaultdict(int)
        
        for r in range(len(s)):
            hmap[s[r]]+=1
            most_freq = max(hmap.values())
            
            while ((r-l+1) - most_freq) > k:
                # contract window
                hmap[s[l]]-=1
                l+=1
            
            # once window is fully contracted, update res
            res = max(res, r-l+1)
            
        return res
        