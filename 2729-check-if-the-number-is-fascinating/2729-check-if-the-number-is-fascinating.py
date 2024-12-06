class Solution:
    def isFascinating(self, n: int) -> bool:
        double = str(2*n)
        triple = str(3*n)
        
        res = str(n) + double + triple
        
        cnt = Counter(res)
        
        for i in range(10):
            if i == 0 and cnt["0"] > 0: return False
            elif cnt[str(i)] > 1: return False
        
        return True