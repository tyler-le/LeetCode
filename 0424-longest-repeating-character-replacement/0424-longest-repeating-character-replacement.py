class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        n = len(s)
        res = 0

        for r in range(n):
            # add to window
            cnt[s[r]]+=1

            # shrink the window
            while r-l+1 - max(cnt.values()) > k:
                cnt[s[l]]-=1
                l+=1
            
            # record the result
            res = max(res, r-l+1)

        return res

