class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        """
        Greedy
        """

        # pairs.sort(key = lambda x : x[1])
        # prev_start, prev_end = pairs[0]
        # res = 1
        # for curr_start, curr_end in pairs[1:]:
        #     if prev_end < curr_start: 
        #         res+=1
        #         prev_end = curr_end
        
        # return res

        
        """
        DP
        """
        pairs.sort(key = lambda x : x[0])
        n = len(pairs)

        dp = [0 for _ in range(n)]
        # dp[i] = maximum chain ending exactly at index i

        for i in range(n):
            take = 1
            leave = dp[i-1] if i-1 >= 0 else 0
            curr_start, curr_end = pairs[i]

            for j in range(i):
                prev_start, prev_end = pairs[j]

                if prev_end < curr_start:
                    take = max(take, 1 + dp[j])

            dp[i] = max(leave, take)
        
        return max(dp)

        

        """
        Recursive
        """
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

