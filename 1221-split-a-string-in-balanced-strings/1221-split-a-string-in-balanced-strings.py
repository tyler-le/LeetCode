class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_left, num_right = 0, 0
        res = 0
        
        for ch in s:
            if ch == "R":
                num_right+=1
            else:
                num_left+=1
            
            if num_left == num_right:
                res+=1
                num_left, num_right = 0, 0
            
        return res