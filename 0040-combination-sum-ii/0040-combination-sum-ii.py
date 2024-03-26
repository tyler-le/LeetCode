class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path, index):
            nonlocal res
            
            if sum(path) == target:
                res.append(path.copy())
                return
            elif index >= len(candidates):
                return
            elif sum(path) > target:
                return
            
            else:
                cand = candidates[index]
                IN = backtrack(path + [cand], index+1)
                
                while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                    index+=1
                
                OUT = backtrack(path, index+1)
            
        candidates.sort()
        backtrack([], 0)
        return res