class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        state = defaultdict(int) # (path, index) : num ways to solve that state
        
        def backtrack(curr, index):
            nonlocal res
            acc = 0
            
            if (curr, index) in state:
                return state[(curr, index)]
            
            if index == n:
                if curr == target: return 1
                else: return 0
            
            acc+=backtrack(curr + nums[index], index+1)
            acc+=backtrack(curr - nums[index], index+1)
            
            state[(curr, index)] = acc
            
            return acc
        
        return backtrack(0, 0)
            