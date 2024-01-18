class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def backtrack(idx, path):
            if sum(path) == target: 
                res.append(path.copy())
                return
            
            if sum(path) > target:
                return
            
            if idx >= len(candidates):
                return
            
            backtrack(idx+1, path + [candidates[idx]])
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            backtrack(idx+1, path)
        
        res = []
        candidates.sort()
        backtrack(0, [])
        return res