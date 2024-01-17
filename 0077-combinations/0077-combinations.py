class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, path):
            if len(path) == k:
                res.append(path.copy())
                return 
            
            if i > n: 
                return
            
            
            backtrack(i+1, path + [i])  # include
            backtrack(i+1, path)        # exclude
            
        backtrack(1, [])
        return res