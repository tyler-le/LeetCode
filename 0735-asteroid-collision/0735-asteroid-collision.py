class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for ast in asteroids:
            survives = True
            while stack and stack[-1] > 0 and ast < 0:
                # ast is lt
                if stack[-1] < abs(ast):
                    stack.pop()
                
                # ast is gt
                elif stack[-1] > abs(ast):
                    survives = False
                    break
                
                # ast is eq
                else:
                    survives = False
                    stack.pop()
                    break
                    
            if survives: 
                stack.append(ast)
                    
        return stack