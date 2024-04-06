class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices_to_remove = set()
        stack = []
        
        for i, ch in enumerate(s):
            if ch == "(": stack.append(i)
            elif ch  == ")":
                if not stack:
                    indices_to_remove.add(i)
                else:
                    stack.pop()
        indices_to_remove = indices_to_remove.union(set(stack))
        
        res = ""
        for i in range(len(s)):
            if i in indices_to_remove: continue
            else: res+=s[i]
        
        return res