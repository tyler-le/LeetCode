class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        
        for i in range (len(nums)):
            while nums[i] != -1 and nums[i] != i:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i]=temp
                
        for i in range (len(nums)):
            if nums[i] == -1:
                return i