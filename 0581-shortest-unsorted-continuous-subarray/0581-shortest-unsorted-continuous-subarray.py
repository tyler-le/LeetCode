class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        leftmost, rightmost = math.inf, 0
        n = len(nums)
        
        for i, curr in enumerate(nums):
            while stack and curr < stack[-1][0]:
                popped_num, popped_idx = stack.pop()
                leftmost = min(leftmost, popped_idx)
            stack.append((nums[i], i))
            
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > stack[-1][0]:
                popped_num, popped_idx = stack.pop()
                rightmost = max(rightmost, popped_idx)
            stack.append((nums[i], i))
        
        if leftmost == float("inf") or rightmost == 0: return 0
        return rightmost - leftmost + 1
        
        