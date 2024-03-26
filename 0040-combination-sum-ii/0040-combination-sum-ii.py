class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def backtrack(idx, path):
            
            # we found a valid combination 
            if sum(path) == target: 
                res.append(path.copy())
                return
            
            # we added too much to the combination
            if sum(path) > target:
                return
            
            # we have no more items to consider
            if idx >= len(candidates):
                return
            
            # dfs on all future elements and include candidates[idx]
            backtrack(idx+1, path + [candidates[idx]])
            
            # after we've considered candidates[idx] at this position, we need to skip over all identical candidates
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            
            # dfs on all future elements and don't include candidates[idx]
            backtrack(idx+1, path)
        
        res = []
        candidates.sort()
        backtrack(0, [])
        return res