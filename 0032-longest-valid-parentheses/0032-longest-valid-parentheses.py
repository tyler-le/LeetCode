class Solution:
    def longestValidParentheses(self, s: str) -> int:
        num_open, num_closed = 0, 0
        res = 0

        for ch in s:
            if ch == "(": num_open+=1
            else: num_closed+=1

            if num_closed > num_open:
                num_open = 0
                num_closed = 0

            elif num_open == num_closed:
                res = max(res, num_open + num_closed)
        

        num_open, num_closed = 0, 0
        for ch in s[::-1]:
            if ch == "(": num_open+=1
            else: num_closed+=1

            if num_closed < num_open:
                num_open = 0
                num_closed = 0

            elif num_open == num_closed:
                res = max(res, num_open + num_closed)
        
        return res

            
