class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_map = Counter(s)
        t_map = Counter(t)
        window = defaultdict(int)
        num_valid = 0
        res = (math.inf, -1, -1)
        l = 0
        needed = len(t_map)
        n = len(s)

        for r in range(n):
            window[s[r]]+=1
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                num_valid+=1

            while l < r and (window[s[l]] > t_map[s[l]]):
                window[s[l]]-=1
                l+=1
            
            if num_valid == needed and r-l+1 < res[0]:
                res = (r-l+1, l, r)
        
        return s[res[1]: res[2]+1]

            