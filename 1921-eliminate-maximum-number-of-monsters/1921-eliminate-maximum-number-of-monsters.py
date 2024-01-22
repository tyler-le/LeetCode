class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        n = len(dist)
        
        # calculate arrival times
        arrivals = [(d/s) for d, s in zip (dist, speed)]
        
        # sort by monsters that arrive soonest
        arrivals.sort()
        
        # if arrivals[i] < i, that means the monster will arrive at time arrivals[i] but since the weapon takes a minute to reload, we need it to arrive at time i or later
        for i, a in enumerate(arrivals):
            if i >= a: return i
            
        return n