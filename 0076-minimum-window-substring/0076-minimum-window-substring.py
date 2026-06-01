class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = Counter(t)
        required = len(t_cnt.keys())
        window_cnt = defaultdict(int)
        conditions_met = 0
        n = len(s)
        l = 0
        res = (math.inf, -1, -1)

        for r in range(n):
            window_cnt[s[r]]+=1
            if window_cnt[s[r]] == t_cnt[s[r]]:
                conditions_met+=1
            
            while conditions_met == required:
                if r-l+1 < res[0]:
                    res = (r-l+1, l, r)

                window_cnt[s[l]]-=1
                if window_cnt[s[l]] == t_cnt[s[l]] - 1:
                    conditions_met-=1
                l+=1
        
        return s[res[1] : res[2] + 1]