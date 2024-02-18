class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # backtracking
        # map (acc, index) : number of ways target can be formed
        # each choice, we can (+) the current num or (-) the current num
        
        def backtrack(index, acc):
            
            if (acc, index) in hmap: 
                return hmap[(acc, index)]
            
            if index >= n:
                if acc == target: 
                    return 1
                return 0
                
            # make a current choice for the index
            add = backtrack(index+1, acc + nums[index])
            sub = backtrack(index+1, acc - nums[index])
            
            hmap[(acc, index)] = (add + sub)
            
            return hmap[(acc, index)]
            
            
        
        n = len(nums)
        hmap = defaultdict(int)
        return backtrack(0, 0)
