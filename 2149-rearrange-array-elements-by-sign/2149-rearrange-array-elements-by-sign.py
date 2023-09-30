class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 0
        res = []
        n = len(nums)
        
        for i in range(n):
            while pos < n and nums[pos] < 0: pos+=1
            while neg < n and nums[neg] >= 0:neg+=1
                
            if i % 2 == 0:
                res.append(nums[pos])
                pos+=1
            else:
                res.append(nums[neg])
                neg+=1
        
        return res
            