class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        res = 0
        
        for num in nums:
            if num + diff in nums_set and num + (2*diff) in nums_set:
                res+=1
        return res