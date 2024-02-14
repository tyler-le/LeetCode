class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_ptr, neg_ptr = 0, 0
        n = len(nums)
        res = []
        
        while pos_ptr < n and neg_ptr < n:
            while nums[pos_ptr] < 0:
                pos_ptr+=1
            while nums[neg_ptr] >= 0:
                neg_ptr+=1
                
            res.append(nums[pos_ptr])
            res.append(nums[neg_ptr])
            pos_ptr+=1
            neg_ptr+=1
            
        return res