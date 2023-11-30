class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(path, cands):
            
            if sum(path) == target:
                res.append(path.copy())
                return
            
            if sum(path) > target:
                return
            
            for i in range(len(cands)):
                cand = cands[i]
                backtrack(path + [cand], cands[i:])
                
        backtrack([], candidates)
        return res
            