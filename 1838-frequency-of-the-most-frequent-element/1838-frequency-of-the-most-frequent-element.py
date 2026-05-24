class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Brute force is easy, but the optimized version involves a sliding window that tracks the cost to turn all elements in the current range into nums[r]. For example, given nums = [1, 4, 8, 13] and k = 5, if our window spans from index 0 to 2 ([1, 4, 8]), the target value is 8. To calculate the new cost efficiently, we take the previous cost required to make the sub-array [1, 4] equal to 4, and simply add the additional effort needed to raise those same two elements from 4 to 8. This incremental update is calculated as the difference between the new and old targets (8 - 4) multiplied by the number of elements currently in the window (2), avoiding the need to re-sum every difference from scratch.
        """
        cost = 0
        n = len(nums)
        l = 0
        res = 1
        nums.sort()

        for r in range(1, n):

            # cost to lift all elems in window to nums[r]
            cost = cost + ((nums[r] - nums[r-1]) * (r-l))

            while cost > k:
                # remove nums[l] from window
                # gives us nums[r] - nums[l] operations back
                cost-=(nums[r] - nums[l])
                l+=1
            
            if cost <= k: 
                res = max(res, r-l+1)

        return res

