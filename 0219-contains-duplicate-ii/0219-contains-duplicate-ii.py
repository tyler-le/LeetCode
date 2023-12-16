class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hmap = dict()

        for i, num in enumerate(nums):
            if num in hmap and i - hmap[num] <= k: 
                return True
            else: hmap[num] = i
            
        return False
        