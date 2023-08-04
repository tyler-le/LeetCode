class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, comb, nxt):
            if remain == 0:
                res.append(comb.copy())
                return
            
            for i in range (nxt, n+1):
                comb.append(i)
                backtrack(remain-1, comb, i+1)
                comb.pop()

        backtrack(k, [], 1)
        return res
            
            