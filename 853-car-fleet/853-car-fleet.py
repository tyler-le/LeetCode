class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        
        times = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        
        fleet_time = 0
        res = 0
        
        for time in reversed(times):
            
            if time > fleet_time: 
                res+=1
                fleet_time = time
                
        return res
        
        