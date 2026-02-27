class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_to_right = []
        right_to_left = deque()
        res = nums[0]
        n = len(nums)
        num_negatives = 0

        curr = 1
        for num in nums:
            if num < 0: num_negatives+=1
            curr*=num
            left_to_right.append(curr)
            if not curr: curr = 1

        curr = 1
        for num in nums[::-1]:
            curr*=num
            right_to_left.appendleft(curr)
            if not curr: curr = 1

        # even num_negatives
        if not num_negatives % 2:
            return max(max(left_to_right), max(right_to_left))
                
        
        else:
            for i in range(n):
                prefix = left_to_right[i-1] if i-1 >= 0 else -math.inf
                suffix = right_to_left[i+1] if i+1 < n else -math.inf
                res = max(res, prefix, suffix)

        return res
    