class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decoded = ""
        
        for ch in s:
            if ch != ']': 
                stack.append(ch)
                continue
                
            while stack[-1] != '[': 
                decoded += stack.pop()

            stack.pop() # pop the '['

            # get the number k (aka num_repeats)
            base = 1
            num_repeats = 0
            while stack and stack[-1].isdigit():
                num_repeats = num_repeats + (int(stack.pop()) - int('0')) * base
                base*=10

            # extend it k-1 more times (k is same as num_repeats)
            decoded = decoded + (decoded * (int(num_repeats) - 1))
            stack.extend(list(reversed(decoded)))
            decoded = ""
                
                
        return "".join(stack)