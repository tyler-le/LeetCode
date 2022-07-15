class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        stack = []
        
        for parens in s:
            if parens == '{': 
                stack.append('}')
            elif parens == '(': 
                stack.append(')')
            elif parens == '[': 
                stack.append(']')            
            else: 
                if len(stack) == 0 or parens != stack.pop():
                    return False
                
        return len(stack) == 0
                