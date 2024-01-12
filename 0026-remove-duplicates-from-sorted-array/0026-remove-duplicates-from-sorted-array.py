class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        insertion = 0
        for scanner in range(n):
            if nums[scanner] != nums[insertion]:
                insertion+=1
                nums[insertion] = nums[scanner]
        return insertion+1