class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            while left < n and nums[left] != val: left+=1
                
            while right >= 0 and nums[right] == val: right-=1
            
            if left <= right and left < n and right >= 0: 
                nums[left], nums[right] = nums[right], nums[left]
        
        return right + 1
            
    