class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        
        for tok in tokens:
            if tok not in operators: stack.append(int(tok))
            
            else:
                y, x = stack.pop(), stack.pop()
                
                if tok == "+": stack.append(x+y)
                elif tok == "-": stack.append(x-y)
                elif tok == "*": stack.append(x*y)
                else: stack.append(int(x / y))
                    
        return stack[0]
                