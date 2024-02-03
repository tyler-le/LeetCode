class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        l = 0
        res = 0
        n = len(s)
        
        for r in range(n):
            hmap[s[r]]+=1
            while len(hmap) > k:
                hmap[s[l]]-=1
                if not hmap[s[l]]: del hmap[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res