class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid: return False
            else: mass+=asteroid
        
        return True