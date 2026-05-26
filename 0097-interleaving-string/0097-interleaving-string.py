class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        
        for p1 in range(n, -1, -1):
            for p2 in range(m, -1, -1):
                if p1 == n and p2 == m: 
                    dp[p1][p2] = True
                
                index = p1 + p2
                
                if p1 < n and s1[p1] == s3[index]:
                    if dp[p1+1][p2]: 
                        dp[p1][p2] |= True

                if p2 < m and s2[p2] == s3[index]:
                    if dp[p1][p2+1]:
                        dp[p1][p2] |= True

        return dp[0][0]

        

        @cache
        def f(index, p1, p2):

            if index == len(s3):
                if p1 == len(s1) and p2 == len(s2):
                    return True
                return False
            
            if p1 < len(s1) and s1[p1] == s3[index]:
                if f(index + 1, p1 + 1, p2): return True
            
            if p2 < len(s2) and s2[p2] == s3[index]:
                if f(index + 1, p1, p2 + 1): return True

            return False

        return f(0, 0, 0)