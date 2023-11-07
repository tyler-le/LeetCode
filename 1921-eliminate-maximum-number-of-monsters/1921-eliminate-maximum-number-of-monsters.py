class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n, res = len(dist), 0
        arrival_times = [(d/s) for d,s in zip(dist, speed)]
        
        arrival_times.sort()
        
        for i in range(n):
            if i >= arrival_times[i]: return res
            else: res+=1
            
        return res