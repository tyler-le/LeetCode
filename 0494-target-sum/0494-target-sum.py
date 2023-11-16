class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:        
        # map (acc, index) : number of ways target can be formed
        dp = collections.defaultdict(int)
        
        def backtrack(acc, index):
            
            # check cache
            if (acc, index) in dp: 
                return dp[(acc, index)]
            
            # base case
            if index == len(nums):
                return 1 if (acc == target) else 0
            
            # make the choice
            num_ways_add = backtrack(acc+nums[index], index+1)   
            
            # make the second choice
            num_ways_sub = backtrack(acc-nums[index], index+1)
            
            # cache the result
            dp[(acc, index)] = num_ways_add + num_ways_sub
            
            return dp[(acc, index)]
            
        return backtrack(0, 0)
            