class Solution:
    def minSteps(self, s: str, t: str) -> int:

        s_cnt, t_cnt = Counter(s), Counter(t)        
        return sum(abs(s_cnt[ch] - t_cnt[ch]) for ch in set(s+t))