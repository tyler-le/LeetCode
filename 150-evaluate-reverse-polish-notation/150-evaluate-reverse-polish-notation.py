class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = set(['+', '-', '*', '/'])
        
        for tok in tokens:
            if tok not in operations: 
                stack.append(int(tok))
            else:
                y, x = stack.pop(), stack.pop()
                if tok == '+': stack.append(x + y)
                elif tok == '-': stack.append(x-y)
                elif tok == '*': stack.append(x*y)
                elif tok == '/': stack.append(int(x / float(y)))
            
        return stack[0]
                