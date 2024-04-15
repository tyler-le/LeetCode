class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # greedy 
        nums.sort()
        n = len(nums)
        res = []
        
        # sort [1,2,3,4,5]
        # interleave nums[left] and nums[right] -> [1,5,2,4,3]
    
        l, r = 0, n-1
        while l < r:
            res.append(nums[l])
            res.append(nums[r])
            l+=1
            r-=1
        
        # if odd length then we need to push in the middle element manually
        if n % 2:
            res.append(nums[l])
        
        return res
            