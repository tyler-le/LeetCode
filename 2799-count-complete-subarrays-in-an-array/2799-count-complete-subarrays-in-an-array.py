class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l = 0
        res = 0
        n = len(nums)
        hmap = defaultdict(int)
        k = len(Counter(nums))
        for r in range(n):
            hmap[nums[r]]+=1
            
            while len(hmap) == k:
                hmap[nums[l]]-=1
                if not hmap[nums[l]]: del hmap[nums[l]]
                l+=1
                res+=len(nums) - r
        return res
            
            
            
            