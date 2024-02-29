class Solution:
    def minSteps(self, s: str, t: str) -> int:
        seen = set()
        s_cnt, t_cnt = Counter(s), Counter(t)
        res = 0
        
        for ch in s:
            if ch in seen: continue
            res+=(abs(s_cnt[ch] - t_cnt[ch]))
            seen.add(ch)
        
        for ch in t:
            if ch in seen: continue
            res+=(abs(t_cnt[ch] - s_cnt[ch]))
            seen.add(ch)
        
        return res