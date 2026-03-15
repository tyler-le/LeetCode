# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        celeb = 0
        
        for person in range(1, n):
            if knows(celeb,person): celeb = person
            

        for person in range(n):
            if person == celeb: continue
            if not knows(person, celeb): return -1
            if knows(celeb, person): return -1

        return celeb