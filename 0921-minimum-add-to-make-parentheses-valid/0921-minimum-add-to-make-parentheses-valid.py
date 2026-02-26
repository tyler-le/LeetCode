class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for ch in s:
            if not stack or ch == "(":
                stack.append(ch)
            else:
                top = stack[-1]
                if top == "(": 
                    stack.pop()
                else:
                    stack.append(ch)
        
        return len(stack)

