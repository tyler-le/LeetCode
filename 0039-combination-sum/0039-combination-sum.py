class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(path, start):
            nonlocal res
            
            if sum(path) == target: 
                res.append(path.copy())
                return
            if sum(path) > target:
                return
            
            for i in range(start, len(candidates)):
                cand = candidates[i]
                backtrack(path + [cand], i)
                
    
        backtrack([], 0)
        return res