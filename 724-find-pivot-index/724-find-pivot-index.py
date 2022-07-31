class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum, prefix_sum = 0, []
        
        for num in nums:
            pre_sum += num
            prefix_sum.append(pre_sum)
        
        total = prefix_sum[-1]
        if total - prefix_sum[0] == 0: return 0
        
        for i in range(1, len(nums)):
            if prefix_sum[i-1] == total-prefix_sum[i]: return i
            
        return -1
            