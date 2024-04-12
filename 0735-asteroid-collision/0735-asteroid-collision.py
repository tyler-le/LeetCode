class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            current_ast_survived = True
            
            # while current asteroid is left and top is right (collision)
            while stack and stack[-1] > 0 and ast < 0:
                
                # current ast beats top ast
                if stack[-1] < abs(ast):
                    stack.pop()
                    
                # asteroids destroy each other
                elif stack[-1] == abs(ast):
                    stack.pop()
                    current_ast_survived = False
                    break
                
                # top asteroid beats current asteroid
                elif stack[-1] > abs(ast):
                    current_ast_survived = False
                    break
            
            if current_ast_survived: 
                stack.append(ast)
            
        return stack
