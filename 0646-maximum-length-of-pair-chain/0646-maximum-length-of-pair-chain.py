class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[0])
        n = len(pairs)

        @cache
        def f(index, prev_end):
            if index == n: return 0

            curr_start, curr_end = pairs[index]
            take = 0
            leave = 0

            # take pairs[index] only if valid with path[-1]
            if curr_start > prev_end:
                take = 1 + f(index + 1, curr_end)
                
            
            # leave pairs[index]
            leave = f(index + 1, prev_end)

            return max(take, leave)

        return f(0, -math.inf)

