class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def backtrack(curr, path):
            if len(path) > k or sum(path) > n:
                return
                        
            if sum(path) == n and len(path) == k:
                res.append(path.copy())
                return
            
                
            for i in range(curr, 10):
                if i in path: return
                path.append(i)
                backtrack(curr+1, path)
                path.pop()
        
        backtrack(1, [])
        return res
    
        
    
            