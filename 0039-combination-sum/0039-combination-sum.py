class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(i, path):
            if sum(path) == target:
                res.append(path.copy())
                return
            
            if sum(path) > target: return
            if i >= len(candidates): return
            
            cand = candidates[i]
            
            backtrack(i, path + [cand])
            backtrack(i+1, path)
        
        backtrack(0, [])
        return res