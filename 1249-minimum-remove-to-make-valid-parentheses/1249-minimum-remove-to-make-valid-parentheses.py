class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = [] # (char, index)
        PARENS = set(["(", ")"])

        for i, ch in enumerate(s):

            if ch in PARENS:
                if not stack or ch == "(": 
                    stack.append((ch, i))
                elif ch == ")":
                    top_ch, _ = stack[-1]
                    if top_ch == "(":
                        stack.pop()
                    else:
                        stack.append((ch, i))


        s = list(s)
        for _, index in stack:
            s[index] = ""
        
        return "".join(s)



