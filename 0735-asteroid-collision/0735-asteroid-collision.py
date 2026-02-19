class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            
            survived = True
            
            # if the asteroids collide
            while stack and stack[-1] > 0 and asteroid < 0:

                # if equal, pop
                if stack[-1] == abs(asteroid): 
                    stack.pop()
                    survived = False
                    break

                # if top > asteroid, keep top
                elif stack[-1] > abs(asteroid): 
                    survived = False
                    break

                # if top < asteroid, pop top and keep asteroid
                else: 
                    stack.pop()
            
            if survived:
                stack.append(asteroid)
        
        return stack