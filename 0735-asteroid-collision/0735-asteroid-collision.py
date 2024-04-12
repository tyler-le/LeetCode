class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            current_ast_survived = True
            
            while stack and stack[-1] > 0 and ast < 0:
                
                if stack[-1] < abs(ast):
                    stack.pop()
                    
                elif stack[-1] == abs(ast):
                    stack.pop()
                    current_ast_survived = False
                    break
                
                else:
                    current_ast_survived = False
                    break
            
            if current_ast_survived: 
                stack.append(ast)
            
        return stack
