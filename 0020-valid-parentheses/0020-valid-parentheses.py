class Solution:
    def isValid(self, s: str) -> bool:
        # map closed : open
        hmap = {")":"(", "}":"{", "]":"["}
        opens = set(hmap.values())
        stack = []
        
        for ch in s:
            if ch in opens:
                stack.append(ch) # push open brace
            else:
                if not stack: return False
                popped = stack.pop()
                
                # check if popped open brace matches 
                # the mapped value to the corresponding closed brace
                if popped != hmap[ch]:
                    return False
                
        return len(stack) == 0
            