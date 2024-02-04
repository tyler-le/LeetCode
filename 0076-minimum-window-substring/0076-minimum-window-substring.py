class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cnt, t_cnt = defaultdict(int), Counter(t)
        required = len(t_cnt)
        conditions_met = 0
        l = 0
        res = [float("inf"), -1, -1]
        
        for r in range(len(s)):
            
            s_cnt[s[r]]+=1
            
            if s_cnt[s[r]] == t_cnt[s[r]]:
                conditions_met+=1
            
            while conditions_met == required:
                if r-l+1 < res[0]:
                    res = [r-l+1, l, r]
                s_cnt[s[l]]-=1
                
                if s[l] in t_cnt and s_cnt[s[l]] < t_cnt[s[l]]:
                    conditions_met-=1
                l+=1
                    
        left, right = res[1], res[2]+1
        return s[left:right]
            