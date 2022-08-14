class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for tok in tokens:
            if tok == '+': 
                stack.append(stack.pop() + stack.pop())
            elif tok == '-': 
                y, x = stack.pop(), stack.pop()
                stack.append(x-y)
            elif tok == '*': 
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                y, x = stack.pop(), stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(tok))
                
        return stack[0]
                
                
                
            
        
                    
                