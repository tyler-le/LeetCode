class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        hmap = {}
        
        for ch in ascii_lowercase:
            hmap[ch] = ch.upper()
            hmap[ch.upper()] = ch
            
        for curr_ch in s:
                        
            if stack and hmap[curr_ch] == stack[-1]: stack.pop()
            else: stack.append(curr_ch)
        
        return "".join(stack)
                
                
                    