class Solution:
    def isValid(self, s: str) -> bool:
        opens = set(["(", "[", "{"])
        closed = set([")", "]", "}"])
        stack = []
        
        hmap = dict()
        hmap[")"] = "("
        hmap["]"] = "["
        hmap["}"] = "{"
        
        for ch in s:
            if ch in opens:
                stack.append(ch)
            else:
                if stack:
                    popped = stack.pop()
                    if popped != hmap[ch]:
                        return False
                else:
                    return False
        return not len(stack)