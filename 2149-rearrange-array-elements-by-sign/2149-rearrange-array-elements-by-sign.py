class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_ptr, neg_ptr = 0, 0
        res = []
        n = len(nums) // 2
        
        for _ in range(n):
            while nums[pos_ptr] < 0: pos_ptr+=1
            while nums[neg_ptr] >= 0: neg_ptr+=1
            
            res.append(nums[pos_ptr])
            res.append(nums[neg_ptr])
            pos_ptr+=1
            neg_ptr+=1
            
        return res