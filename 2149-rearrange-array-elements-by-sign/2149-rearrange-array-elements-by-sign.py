class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        pos_ptr = 0
        neg_ptr = 0
        
        while len(res) != len(nums):
            while pos_ptr < n and nums[pos_ptr] < 0:
                pos_ptr+=1
            
            while neg_ptr < n and nums[neg_ptr] >= 0:
                neg_ptr+=1
                
            if pos_ptr < n and neg_ptr < n:
                res.append(nums[pos_ptr])
                res.append(nums[neg_ptr])
            
            pos_ptr+=1
            neg_ptr+=1
        
        return res