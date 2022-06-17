class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        nums.append(-1)
        
        for i in range(len(nums)):
            while nums[i]!=-1 and nums[i]!=i:
                if nums[nums[i]]==nums[i]:
                    nums[i]=-1
                    break
                else:
                    temp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i]=temp
                    
        for i in range(1, len(nums)):
            if nums[i] == -1:
                res.append(i)
                
        return res
    
            
        