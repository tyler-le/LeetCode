class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start, path, curr_sum):
            nonlocal res

            if curr_sum == target:
                res.append(path.copy())
                return

            if curr_sum > target:
                return

            for i in range(start, n):
                # we do start > n because we don't want to skip on the first element
                # aka (candidates[start]).
                # only skip on duplicate elements AFTER first element
                if (i > start) and (candidates[i] == candidates[i-1]): 
                    continue
                    
                path.append(candidates[i])
                curr_sum+=candidates[i]
                backtrack(i + 1, path, curr_sum)
                path.pop()
                curr_sum-=candidates[i]
            
        
        backtrack(0, [], 0)
        return res