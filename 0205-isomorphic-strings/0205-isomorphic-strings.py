class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = defaultdict(str)
        t_to_s = defaultdict(str)
        
        for ch1, ch2 in zip(s, t):
            if ch1 not in s_to_t and ch2 not in t_to_s:
                s_to_t[ch1] = ch2
                t_to_s[ch2] = ch1
            elif s_to_t[ch1] != ch2 or t_to_s[ch2] != ch1:
                return False
        
        return True