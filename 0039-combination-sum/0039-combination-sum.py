class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(i, path):

            if sum(path) == target:
                res.append(path.copy())
                return
            
            elif sum(path) > target:
                return
            
            elif i >= len(candidates):
                return 
            
            else:
                backtrack(i, path + [candidates[i]])     # continue with this element included
                backtrack(i+1, path)                     # continue without this element included 
                
        res = []
        backtrack(0, [])
        return res
    