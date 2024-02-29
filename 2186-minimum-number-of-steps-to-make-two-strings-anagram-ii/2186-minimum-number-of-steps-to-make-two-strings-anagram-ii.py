class Solution:
    def minSteps(self, s: str, t: str) -> int:

        s_cnt, t_cnt = Counter(s), Counter(t)
        res = 0
        chars = set(s+t)
        
        for ch in chars:
            res+=abs(s_cnt[ch] - t_cnt[ch])
        
        return res