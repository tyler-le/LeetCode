class Solution:
    def minSwaps(self, s: str) -> int:
        # count the number of mismatches
        mismatches = 0
        stack = []
        for ch in s:
            if ch == "[":
                stack.append("[")
            else:
                if not stack: mismatches+=1
                else: stack.pop()
                    
        return (mismatches+1) // 2