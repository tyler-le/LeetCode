class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
                
        stack = []
        
        for ast in asteroids:

           # rightward ast, add to stack
            if ast > 0:
                stack.append(ast)
                
            # leftward ast, handle collision
            else:
                # if stack is empty or has leftward asteroid as top, 
                # then no collision and add to stack
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                    
                else:
                    # stack is not empty or has rightward asteroid as top, 
                    # simulate collisions
                    
                    while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                        # top is colliding with ast and top is smaller, so remove from stack
                        stack.pop()

                    if stack and stack[-1] == abs(ast):
                        # top is equal to ast, so destroy both
                        stack.pop()

                    elif stack and stack[-1] < 0 and ast < 0:
                        # top is smaller than ast, so add ast
                        stack.append(ast)
                        
                    elif not stack:
                        # ast cleared out entire stack, add ast to stack
                        stack.append(ast)

        return stack
                
                