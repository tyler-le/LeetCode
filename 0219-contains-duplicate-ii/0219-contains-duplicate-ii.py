class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hmap = dict()

        for i, num in enumerate(nums):
            # check if we found a pair
            if num in hmap and i - hmap[num] <= k: return True
            
            # if (i - hmap[num] > k) then we need to replace 
            # the value of hmap[num] with 'i'
            else: hmap[num] = i
            
        return False
        