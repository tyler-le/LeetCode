class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        
        sum_left, sum_right = left, right
        
        if n == 1: return 1
        
        while left < right:
            if sum_left < sum_right:
                sum_left += left + 1
                left += 1

            else:
                sum_right += right - 1
                right -= 1
            
            if sum_left == sum_right and left + 1 == right - 1:
                return left + 1
            
        
        return -1