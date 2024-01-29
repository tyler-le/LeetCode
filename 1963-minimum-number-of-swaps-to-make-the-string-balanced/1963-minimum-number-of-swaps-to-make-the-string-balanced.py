class Solution:
    def minSwaps(self, s: str) -> int:
        # get rid of the balanced portion and count the mismatches
        
        stack = []
        mismatches = 0
        
        for ch in s:
            if ch == "[":
                stack.append("[")
            else:
                if stack: stack.pop()
                else: mismatches+=1
        
        return (mismatches + 1) // 2
            