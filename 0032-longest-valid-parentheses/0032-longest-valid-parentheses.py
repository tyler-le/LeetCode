class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        n = len(s)
        OPEN, CLOSED = "(", ")"
        res = 0

        for i, ch in enumerate(s):
            if ch == OPEN:  
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: res = max(res, i - stack[-1])
            
        return res