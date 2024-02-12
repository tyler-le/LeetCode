class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left_boundary, right_boundary = float("inf"), 0
        stack, n = [], len(nums)
        
        for i in range(n):
            curr = nums[i]
            while stack and curr < stack[-1][1]:
                popped = stack.pop()
                left_boundary = min(left_boundary, popped[0])
                
            stack.append((i, curr))
            
        stack = []
        for i in range(n-1, -1, -1):
            curr = nums[i]
            while stack and curr > stack[-1][1]:
                popped = stack.pop()
                right_boundary = max(right_boundary, popped[0])
            
            stack.append((i, curr))
            
        if left_boundary == float("inf") or right_boundary == 0: return 0
        return right_boundary - left_boundary + 1