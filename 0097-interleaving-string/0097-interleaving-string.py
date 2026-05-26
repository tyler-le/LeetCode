class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

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