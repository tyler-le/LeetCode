class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        hmap = collections.defaultdict(int)
        l = res = 0
        
        for r in range(len(s)):
            hmap[s[r]]+=1
            
            while len(hmap) > k:
                hmap[s[l]]-=1
                if not hmap[s[l]]:
                    del hmap[s[l]]
                l+=1
            res = max(res, r-l+1)
        
        return res
        