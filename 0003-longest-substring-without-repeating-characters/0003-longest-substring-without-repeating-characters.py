class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # scan thru s
        # keep track of character counts
        # if a character count > 2, shrink window from left until valid window
        # record width and take the max
        
        l = 0
        res = 0
        hmap = defaultdict(int)
        
        for r in range(len(s)):
            hmap[s[r]]+=1    
            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            
        return res