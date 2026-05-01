class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        costs = {}
        chars = list(chars)

        for i in range(n):
            if s[i] not in chars:
                costs[s[i]] = 1 + (ord(s[i]) - ord('a'))
            elif s[i] in chars and s[i] not in costs:
                costs[s[i]] = vals[chars.index(s[i])]

        # kadanes algorith / greedy

        l = 0
        curr_cost = 0
        res = -math.inf

        for r in range(n):

            # choose to start over
            if curr_cost + costs[s[r]] <= costs[s[r]]:
                curr_cost = costs[s[r]]
            else:
                curr_cost+=costs[s[r]]
            
            res = max(res, curr_cost, 0)
        
        return res

