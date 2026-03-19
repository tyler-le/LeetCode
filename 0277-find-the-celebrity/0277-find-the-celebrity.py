# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # celebrity is known by everyone
        # celebrity knows nobody

        # knows(a, b) is true -> a cannot be celebrity
        # knows(a, b) is false -> b cannot be celebrity

        candidate = 0

        for person in range(1, n):
            if knows(candidate, person): 
                candidate = person
        
        for person in range(n):
            if candidate == person: continue
            if knows(candidate, person): return -1
            if not knows(person, candidate): return -1

        return candidate

