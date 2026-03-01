class Solution:
    def minCost(self, n: int) -> int:
        # backtracking with cache

        cache = {}

        # backtrack(num) -> min cost to split num
        def backtrack(num):
            
            res = math.inf

            if num == 1: 
                return 0
            if num == 2: 
                return 1

            if num in cache:
                return cache[num]

            min_cost = (math.inf, -1, -1) # (cost, a, b)

            for i in range(1, num):
                # split
                a = i
                b = num - i

                # for each pair find the pair with minimum cost
                cost_a = backtrack(a)
                cost_b = backtrack(b)

                if cost_a + cost_b < min_cost[0]:
                    min_cost = (cost_a + cost_b, a, b)

            # for the min cost pair, return a*b
            cache[num] = (min_cost[1] * min_cost[2]) + min_cost[0]
            return (min_cost[1] * min_cost[2]) + min_cost[0]

        return backtrack(n) 