class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using XOR to find pairs

        xor = nums[0]
        for num in nums[1:]:
            xor ^= num
        return xor
        