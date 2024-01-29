class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
       # [0, 1, 3, 5, 5]
    
        res = 0
        nums.sort()
        
        for left in range(len(nums)):
            if not nums[left]: continue
            sub = nums[left]
            for right in range(left, len(nums)):
                nums[right]-=sub
            res+=1
            
            if not nums[-1]: 
                return res
        return 0
                
    
    
            