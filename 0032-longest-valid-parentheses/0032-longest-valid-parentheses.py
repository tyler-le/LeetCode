class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        OPEN, CLOSED = "(", ")"
        res = 0


        # The idea is to keep track of the boundary
        for i, ch in enumerate(s):

            if ch == OPEN:
                stack.append(i)
            else:

                # pop from stack and determine boundary validity
                stack.pop()

                # if popping leads the stack to be empty 
                # that means it hit the boundary
                # which means it is invalid, so we update the boundary
                if not stack:
                    stack.append(i)

                # if popping does not lead the stack to be empty
                # then we did not hit the boundary
                # so we update the result
                else:
                    res = max(res, i - stack[-1])
        
        return res

