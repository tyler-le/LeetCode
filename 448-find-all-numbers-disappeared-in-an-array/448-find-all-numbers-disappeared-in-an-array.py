class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = []
        res = []
        
        for index in range(len(nums)+1):
            count.append(0)
            
        for index in range(len(nums)):
            count[nums[index]]+=1
            
        for index in range(1,len(count)):
            if count[index] == 0:
                res.append(index)
                
        return res
            
        