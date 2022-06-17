class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = []
        res = []
        
        # mark all vals in count as 0
        for index in range(len(nums)+1):
            count.append(0)
            
        # loop through nums and record each value as the index in count   
        for index in range(len(nums)):
            count[nums[index]]+=1
            
        # if any value in count is 0, the value of the index is missing from nums
        for index in range(1,len(count)):
            if count[index] == 0:
                res.append(index)
                
        return res
    
            
        