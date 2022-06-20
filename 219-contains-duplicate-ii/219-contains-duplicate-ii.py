class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                if abs(hashmap.get(n) - i) <= k:
                    return True
            hashmap[n] = i
        return False