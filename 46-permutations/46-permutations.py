class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack():
            if len(nums) == len(permutation):
                res.append(permutation[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    permutation.append(nums[i])
                    used[i] = True
                    
                    backtrack()
                    
                    permutation.pop()
                    used[i] = False
        
        used, res, permutation = [False] * len(nums), [], []
        backtrack()
        return res