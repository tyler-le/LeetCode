class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def f(index, prev_color):
            if index == n: return 0
            res = math.inf

            for i in range(len(costs[index])):
                if i == prev_color: continue
                subproblem = f(index + 1, i)
                total = costs[index][i] + subproblem
                res = min(res, total)
            
            return res
        
        return f(0, None)