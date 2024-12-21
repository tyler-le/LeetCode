class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = set(["+", "-", "/", "*"])
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                x, y = stack.pop(), stack.pop()
                if tok == "+": stack.append(x+y)
                elif tok == "-": stack.append(y-x)
                elif tok == "/": stack.append(int(y/x))
                else: stack.append(x*y)
        return stack.pop()


