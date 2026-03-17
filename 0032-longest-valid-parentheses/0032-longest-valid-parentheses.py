class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        OPEN, CLOSED = "(", ")"
        num_open, num_closed = 0, 0
        res = 0

        for i, ch in enumerate(s):
            if ch == OPEN:
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        
        return res

        