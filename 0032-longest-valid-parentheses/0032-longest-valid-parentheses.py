class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        OPEN, CLOSED = "(", ")"
        res = 0

        num_open, num_closed = 0, 0
        for i, ch in enumerate(s):
            if ch == OPEN: num_open+=1
            else: num_closed+=1

            if num_closed > num_open:
                num_open = 0
                num_closed = 0

            elif num_closed == num_open:
                res = max(res, num_open + num_closed)

        num_open, num_closed = 0, 0
        for i, ch in enumerate(s[::-1]):
            if ch == OPEN: num_open+=1
            else: num_closed+=1

            if num_closed < num_open:
                num_open = 0
                num_closed = 0

            elif num_closed == num_open:
                res = max(res, num_open + num_closed)
        
        return res