class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(path, idx):
            nonlocal res
            
            if sum(path) == target:
                res.append(path.copy())
                return
            
            elif sum(path) > target:
                return
            
            elif idx >= len(candidates):
                return
            
            else:
                cand = candidates[idx]
                backtrack(path + [cand], idx)
                backtrack(path, idx+1)
        
        backtrack([], 0)
        return res