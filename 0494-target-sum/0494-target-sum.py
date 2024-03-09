class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # for each num, we can backtrack o +num and -num
        res = 0
        n = len(nums)
        state = defaultdict(int) # (curr_sum, index) -> number of ways
        
        
        def backtrack(curr, i):
            nonlocal res
            acc = 0
            if (curr, i) in state: return state[(curr, i)]
            
            if i >= n: 
                if curr == target: return 1
                else: return 0            
                
            acc+=backtrack(curr + nums[i], i+1)
            acc+=backtrack(curr - nums[i], i+1)
            
            state[(curr, i)] = acc
            return acc
            
            
            
        return backtrack(0, 0)
            
        