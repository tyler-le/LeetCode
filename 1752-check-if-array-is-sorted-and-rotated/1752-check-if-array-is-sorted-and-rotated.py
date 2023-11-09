class Solution:
    def check(self, nums: List[int]) -> bool:
        n, allowed = len(nums), 0
        
        for i in range(1, n+1):
            prev, curr = nums[(i-1) % n], nums[i%n]
            if prev > curr: allowed+=1
            if allowed > 1: return False
        
        return True
            