class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        l = 0
        n = len(s)
        res = 0

        for r in range(n):
            hmap[s[r]]+=1

            while hmap[s[r]] > 1:
                hmap[s[l]]-=1
                l+=1
            
            if hmap[s[r]] <= 1:
                res = max(res, r-l+1)
        return res