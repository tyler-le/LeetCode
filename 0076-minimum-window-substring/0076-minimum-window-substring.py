class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0
        res = [-math.inf, math.inf]
        n = len(s)
        t_cnt = Counter(t)
        window_cnt = defaultdict(int)

        conditions_met, conditions_needed = 0, len(t_cnt)

        for r in range(n):
            # extend the window
            window_cnt[s[r]]+=1
            if window_cnt[s[r]] == t_cnt[s[r]]:
                conditions_met+=1

            # shrink the window
            while l < r and (s[l] not in t_cnt or window_cnt[s[l]] > t_cnt[s[l]]):
                window_cnt[s[l]]-=1
                if not window_cnt[s[l]]: del window_cnt[s[l]]
                l+=1

            # check validity and record res
            if conditions_met == conditions_needed and r-l+1 < (res[1] - res[0] + 1):
                res = [l, r]
        
        print(res)
        if res == [-math.inf, math.inf]: return ""
        return s[res[0]:(res[1] + 1)]
