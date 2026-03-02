class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    stack.append(int(x/y))
        
        return stack[0]
