class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for curr_ch in s:
            
            curr_case = curr_ch.islower()
            
            if stack and stack[-1][0].lower() == curr_ch.lower() and curr_case != stack[-1][1]:
                stack.pop()
            else:
                stack.append((curr_ch, curr_case))
        
        return "".join([ch for (ch, _) in stack])
                
                
                    