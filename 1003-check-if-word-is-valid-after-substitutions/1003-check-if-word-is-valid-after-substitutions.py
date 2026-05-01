class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for ch in s:
            stack.append(ch)
            m = len(stack)
            if len(stack) >= 3 and stack[m-3:m] == ["a", "b", "c"]:
                for _ in range(3):
                    stack.pop()
        
        return not stack