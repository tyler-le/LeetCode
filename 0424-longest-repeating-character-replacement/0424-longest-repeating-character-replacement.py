class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window_cnt = defaultdict(int)
        n = len(s)
        res = 0

        for r in range(n):
            window_cnt[s[r]]+=1

            while (r-l+1) - max(window_cnt.values()) > k:
                window_cnt[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
        
        return res