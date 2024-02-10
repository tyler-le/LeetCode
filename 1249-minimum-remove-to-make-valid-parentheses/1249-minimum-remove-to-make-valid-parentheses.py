class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        res = ""
        
        for i, ch in enumerate(s):
            if ch not in "()": continue
            elif ch == "(": stack.append(i)
            elif stack and ch == ")": stack.pop()
            else: indices_to_remove.add(i)
        
        indices_to_remove = indices_to_remove.union(set(stack))
        
        for i, ch in enumerate(s):
            if i in indices_to_remove: continue
            res+=ch
        
        return res