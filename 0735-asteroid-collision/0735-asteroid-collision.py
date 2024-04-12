class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
                
        stack = []
        
        for ast in asteroids:

           # rightward ast
            if ast > 0:
                stack.append(ast)
                
            # leftward ast
            else:
                
                # if stack is empty, no collision, add to stack
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                    
                else:
                    
                    
                    # stack is not empty, simulate collisions
                    while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                        stack.pop()

                    if stack and stack[-1] == abs(ast):
                        stack.pop()

                    elif stack and stack[-1] < abs(ast):
                        stack.append(ast)
                        
                    elif not stack:
                        stack.append(ast)

        return stack
                
                