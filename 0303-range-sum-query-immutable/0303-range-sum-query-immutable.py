class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(self.n):
            if left <= i <= right:
                res+=self.nums[i]
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)