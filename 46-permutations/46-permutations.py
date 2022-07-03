class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
    
        res = []
        
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            removed = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(removed)
                res.append(perm)
                
            nums.append(removed)
            
        return res
        
