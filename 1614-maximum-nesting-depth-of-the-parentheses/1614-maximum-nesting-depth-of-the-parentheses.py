class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        curr_depth = 0
        res = 0
        
        for ch in s:
            if ch == "(":
                curr_depth+=1
                stack.append(("(", curr_depth))
                
            elif ch == ")":
                if stack:
                    stack.pop()
                    curr_depth-=1
                    
            res = max(res, curr_depth)
            
        return res
        