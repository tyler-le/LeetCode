class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        pos_ptr, neg_ptr = 0, 0

        for i in range(n):
            while pos_ptr < n and nums[pos_ptr] < 0: 
                pos_ptr+=1
            while neg_ptr < n and nums[neg_ptr] > 0:
                neg_ptr+=1
            
            if i % 2 == 0:
                arr.append(nums[pos_ptr])
                pos_ptr+=1
            else:
                arr.append(nums[neg_ptr])
                neg_ptr+=1

        return arr