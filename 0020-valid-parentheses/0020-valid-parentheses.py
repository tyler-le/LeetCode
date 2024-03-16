class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        OPEN = set(['(', '[', '{'])
        CLOSED = set([')', ']', '}'])
        hmap = {}
        hmap[")"] = "("
        hmap["}"] = "{"
        hmap["]"] = "["
        
        for ch in s:
            if ch in OPEN:
                stack.append(ch)
            else:
                if not stack: return False
                popped = stack.pop()
                if hmap[ch] != popped: return False
                
        return not stack