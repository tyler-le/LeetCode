class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        l = 0
        n = len(s)
        hmap = defaultdict(int)
        
        for r in range(n):
            
            hmap[s[r]]+=1
            while len(hmap.values()) > 2:
                hmap[s[l]]-=1
                if not hmap[s[l]]:
                    del hmap[s[l]]
                l+=1
            res = max(res, r-l+1)
            
        return res
            