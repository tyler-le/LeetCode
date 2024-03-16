class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sums = defaultdict(int)
        prefix_sum = 0
        res = -math.inf
        prefix_sums[0] = -1
        
        for i in range(len(nums)):
            prefix_sum+=1 if nums[i] else -1
            if prefix_sum in prefix_sums:
                res = max(res, i - prefix_sums[prefix_sum])
            else:
                prefix_sums[prefix_sum] = i
        
        return res if res != -math.inf else 0
            
            
            
            
            