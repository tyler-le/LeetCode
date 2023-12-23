class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         [1,7,3,6,5,6]
#         left  0  1  18  11  17  22
#         right 22 21 14  11   5   0
        
        n = len(nums)
        left = [0] * n
        right = [0] * n
        
        for i in range(n-1):
            left[i+1] = left[i] + nums[i]
        
        for i in range(n-2, -1, -1):
            print(i)
            right[i] = right[i+1] + nums[i+1]
        
        for i, (l, r) in enumerate(zip(left, right)):
            if l == r: return i
            
        return -1