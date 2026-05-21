class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []

        def is_pal(l, r):
            while l <= r:
                if s[l] != s[r]: return False
                l+=1
                r-=1
            return True
        
        def f(start, path):

            if start == n:
                res.append(path.copy())
                return

            for end in range(start, n):
                if is_pal(start, end):
                    path.append(s[start:end+1])
                    f(end + 1, path)
                    path.pop()
        
        f(0, [])
        return res
            