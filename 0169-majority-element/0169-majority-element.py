class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)
        
        for num in nums:
            if count[num] > floor(n / 2): 
                return num