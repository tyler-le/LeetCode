class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1} # sum : freq (base case)
        res, prefix_sum = 0, 0
        
        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            if target in count: res += count[target]
            count[prefix_sum] = 1 + count.get(prefix_sum, 0)
            
        return res
                
            