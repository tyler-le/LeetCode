class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.append(-1)
        
        for i in range(len(nums)):
            while nums[i]!=-1 and nums[i]!=i:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i]=temp