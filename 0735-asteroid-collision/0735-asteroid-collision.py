class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            
            survived = True
            
            while stack and stack[-1] > 0 and ast < 0:
                
                # top ast is smaller than curr ast
                if stack[-1] < abs(ast):
                    stack.pop()
                
                # top as is bigger than curr ast
                elif stack[-1] > abs(ast):
                    survived = False
                    break
                
                # they tie
                else:
                    stack.pop()
                    survived = False
                    break
                    
            if survived:
                stack.append(ast)
                
        return stack
                