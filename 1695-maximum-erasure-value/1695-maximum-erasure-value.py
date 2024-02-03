class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        l = 0
        n = len(nums)
        acc = 0
        res = 0
        
        for r in range(n):
            hmap[nums[r]]+=1
            acc+=nums[r]
            while hmap[nums[r]] > 1:
                acc-=nums[l]
                hmap[nums[l]]-=1
                l+=1
            res = max(res, acc)
        return res
            
            