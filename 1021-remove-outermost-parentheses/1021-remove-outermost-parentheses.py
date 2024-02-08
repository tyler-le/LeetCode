class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # when num_open == num_closed -> primitive parens
                
        res = ""
        num_open, num_closed = 0, 0
        l, r = 0, 0
        
        for ch in s:
            if ch == "(":
                num_open+=1
            else:
                num_closed+=1
            
            if num_closed == num_open:
                res+="".join(s[l+1:r])
                num_closed, num_open = 0, 0
                l=r+1
                
            r+=1
                
        return res