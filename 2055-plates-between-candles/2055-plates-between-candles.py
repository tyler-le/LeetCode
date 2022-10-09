class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        p = [i for i in range(len(s)) if s[i] == '|']
        res = []
        for f,t in queries: 
            l = bisect.bisect_left(p, f)
            r = bisect.bisect_right(p, t)
            print(l,r)
            res.append(p[r-1] - p[l] + 1 - (r - l) if r > l else 0)

        return res