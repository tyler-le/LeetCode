class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = set()
        res = ""
        num_open = 0
        
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
                num_open+=1
            elif ch == ")":
                if not num_open:
                    indices_to_remove.add(i)
                else:
                    stack.pop()
                    num_open-=1
        
        indices_to_remove.update(set(stack))
        
        
        for i in range(len(s)):
            if i not in indices_to_remove:
                res+=s[i]
                        
        return res