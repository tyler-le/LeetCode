class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for tok in tokens:
            if tok in operators:
                y, x = int(stack.pop()), int(stack.pop())
                val = 0
                
                if tok == "+": val = x + y
                elif tok == "-": val = x - y
                elif tok == "*": val = x * y
                else: val = int(x / y)
                stack.append(val)
                
            else:
                stack.append(tok)
                
        return int(stack.pop())
        