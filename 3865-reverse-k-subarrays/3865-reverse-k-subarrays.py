class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        res = []
        n = len(nums)
        window = deque()
        k = n // k

        
        for i in range(0, n, k):
            subarray = []
            for j in range(k):
                subarray.append(nums[i+j])

            for x in subarray[::-1]:
                res.append(x)
        
        return res
