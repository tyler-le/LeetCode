class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)

        def f(index, target, path):
            nonlocal res

            if index == n:
                if target == 0:
                    res.append(path.copy())
                return
            
            if target < 0:
                return

            f(index, target - candidates[index], path + [candidates[index]])
            f(index + 1, target, path)
    
        f(0, target, [])
        return res
