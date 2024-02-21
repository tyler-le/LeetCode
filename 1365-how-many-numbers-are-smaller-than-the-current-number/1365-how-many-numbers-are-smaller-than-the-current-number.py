class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        # [8,1,2,2,3]
        # [1,2,2,3,8]
        cp = nums.copy()
        cp.sort()
        hmap = {}
        
        for i, num in enumerate(cp):
            if num not in hmap:
                hmap[num] = i
            
        for num in nums:
            res.append(hmap[num])
        
        return res
        