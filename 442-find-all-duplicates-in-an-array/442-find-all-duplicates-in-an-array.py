class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.append(-1)
        res = []
        
        for i in range(len(nums)):
            while nums[i]!=-1 and nums[i]!=i:
                if nums[i]==nums[nums[i]] and nums[i]!=-1:
                    res.append(nums[i])
                    nums[i]=-1
                    break
                else:
                    temp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i]=temp
                      
        return res
        