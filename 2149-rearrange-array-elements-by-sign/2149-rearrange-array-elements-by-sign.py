class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        pos, neg = 0, 0
        
        while pos < n or neg < n:
            while pos < n and nums[pos] < 0: pos+=1
            while neg < n and nums[neg] >= 0: neg+=1
            
            if pos < n: res.append(nums[pos])
            if neg < n: res.append(nums[neg])
            pos+=1
            neg+=1
            
        return res
            