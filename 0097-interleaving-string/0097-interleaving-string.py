class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        @cache
        def f(i, j, k):

            if k == len(s3):
                if i == len(s1) and j == len(s2): return True
                else: return False
            
            print(i,j,k)
            if i < len(s1) and k < len(s3) and s1[i] == s3[k] and f(i+1, j, k+1): return True
            elif j < len(s2) and k < len(s3) and s2[j] == s3[k] and f(i, j+1, k+1): return True
            else: return False
            

        return f(0,0,0)