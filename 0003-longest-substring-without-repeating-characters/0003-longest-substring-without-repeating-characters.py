class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        hmap = collections.defaultdict(int)
        res = 0
        
        for r in range(len(s)):
            hmap[s[r]]+=1
            
            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res
            