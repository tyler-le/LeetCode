class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        res = []
        left_max = [nums[0]]
        right_max = deque()

        for i in range(1, n):
            left_max.append(max(left_max[i-1], nums[i]))

        for i in range(n-1, -1, -1):
            if not right_max: right_max.appendleft(nums[i])
            else: right_max.appendleft(max(right_max[0], nums[i]))

        for i in range(n):
            curr = nums[i]

            valid_before = curr > left_max[i-1] if i-1 >= 0 else True
            valid_after = curr > right_max[i+1] if i+1 < n else True

            if valid_before or valid_after:
                res.append(curr)
        
        return res

