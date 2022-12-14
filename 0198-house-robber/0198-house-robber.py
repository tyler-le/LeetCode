class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        A = [0] * (n+1)
        
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        A[0] = nums[0]
        A[1] = max(nums[0], nums[1])
        
        for i in range(2, n+1):
            if (i < n): IN = A[i-2] + nums[i]
            else: IN = A[i-2]
            OUT = A[i-1]
            A[i] = max(IN, OUT)
        
        return A[n]