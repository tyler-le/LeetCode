class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        n = len(s)
        res = 0
        
        for r in range(n):
            cnt[s[r]]+=1
            
            while len(cnt) > k:
                cnt[s[l]]-=1
                if not cnt[s[l]]: del cnt[s[l]]
                l+=1
            
            res = max(res, r-l+1)
        
        return res