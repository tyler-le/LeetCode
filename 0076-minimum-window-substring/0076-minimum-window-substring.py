class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt, s_cnt = Counter(t), defaultdict(int)
        conditions_met, required = 0, len(t_cnt.items())
        l = 0
        res = [float("inf"), -1, -1]
        
        for r in range(len(s)):
            s_cnt[s[r]]+=1
            if s_cnt[s[r]] == t_cnt[s[r]]:
                conditions_met+=1
            
            while l <= r and conditions_met == required:
                if r - l + 1 < res[0]: res = [r-l+1, l, r]
                s_cnt[s[l]]-=1
                if s_cnt[s[l]] < t_cnt[s[l]]: conditions_met-=1    
                l+=1
        print(res)
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]
            
            
                