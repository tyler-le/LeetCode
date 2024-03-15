class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n == 1: return 1
        
        sum_left = 1
        sum_right = n
        l, r = 1, n
        
        while l < r:
            if sum_left >= sum_right:
                r-=1
                sum_right+=r
                
            else:
                l+=1
                sum_left+=l
        
            
            if sum_left == sum_right and l+1 == r-1:
                return l+1
        
        return -1