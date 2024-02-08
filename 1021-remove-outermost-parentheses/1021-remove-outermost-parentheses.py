class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # when num_open == num_closed -> primitive parens
        
        
        # "(()())(())"
        
        res = ""
        curr = []
        num_open, num_closed = 0, 0
        
        for ch in s:
            if ch == "(":
                num_open+=1
                curr.append("(")
            else:
                num_closed+=1
                curr.append(")")
            
            if num_closed == num_open:
                res+="".join(curr[1:len(curr) - 1])
                num_closed, num_open = 0, 0
                curr = []
                
        return res