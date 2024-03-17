class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 1 -> +1
        # 0 -> -1
        
        prefix_sums = {}
        prefix_sums[0] = -1
        acc = 0
        res = 0
        
        for i in range(len(nums)):
            num = nums[i]
                    
            acc = acc + 1 if num else acc - 1
            
            if acc in prefix_sums: res = max(res, i - prefix_sums[acc])
            else: prefix_sums[acc] = i
        
        return res
        