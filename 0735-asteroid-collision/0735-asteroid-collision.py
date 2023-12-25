class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        stack = []
        
        for x in asteroids:
            if x >= 0: stack.append(x)
            else:
                while len(stack) >= 1 and abs(stack[-1]) < abs(x):
                    stack.pop()
                
                if not len(stack):
                    res.append(x)
                else:
                    if stack[-1] == abs(x):
                        stack.pop()
        res+=stack
        return res