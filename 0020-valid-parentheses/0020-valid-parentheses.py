class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
                ")":"(", 
                "}":"{", 
                "]":"["
               }
        
        stack = []
        
        
        for ch in s:
            if ch in hmap.values():
                stack.append(ch)
            else:
                if not stack: return False
                popped = stack.pop()
                if popped != hmap[ch]:
                    return False
                
        return len(stack) == 0
            