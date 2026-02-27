class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        res, n = 0, len(nums)
        cache = {}

        def backtrack(index, curr_sum):
            nonlocal res, n, cache

            cnt = 0

            if index == n:
                if curr_sum == target: 
                    return 1
                else:
                    return 0

            if (index, curr_sum) in cache:
                res+=cache[(index, curr_sum)]

            cnt+=backtrack(index + 1, curr_sum + nums[index])
            cnt+=backtrack(index + 1, curr_sum - nums[index])
            cache[(index, curr_sum)] = cnt

            return cnt
            
        
        return backtrack(index = 0, curr_sum = 0)
