class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; 

        A = nums
        
        for i in range(1, len(nums)):
            IN = nums[i] + A[i-1]
            OUT = nums[i]
            A[i] = max(IN, OUT)
            
        return max(A)
        