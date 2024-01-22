class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
#         dist = [3,2,4]              speed = [5,3,2]
#         miles                       miles/hr
        
#         1 hr (index) 
#         2 miles away (dist)
#         3 miles/hr
        
        arrivals = []
        n = len(dist)
        
        for i, (dist, speed) in enumerate(zip(dist, speed)):
            arrivals.append(dist / speed)
        
        arrivals.sort()
        
        
        for i, a in enumerate(arrivals):
            if i >= a:
                return i
            

        return n