class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        n = len(s)
        hmap = defaultdict(int)

        for r in range(n):
            hmap[s[r]]+=1

            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res
