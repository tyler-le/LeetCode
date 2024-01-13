class Solution:
    def minSteps(self, s: str, t: str) -> int:

        
#         a - 1
#         b - 2
        
#         a - 2
#         b - 1
        
#         1
        
        s1, t1 = Counter(s), Counter(t)
        res = 0
        for ch in s1.keys():
            if s1[ch] > t1[ch]:
                res+=(s1[ch]-t1[ch])
        return res
        