class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        
        for ch in s:
            if ch == "(":
                stack.append("(")
            else:
                if stack: stack.pop()
                else: res+=1
        
        
        return len(stack) + res