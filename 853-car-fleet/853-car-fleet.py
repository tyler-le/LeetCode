class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()
            
        fleet_time, res = 0, 0
        
        for pos, speed in reversed(pairs):
            time = float(target - pos) / speed
            if time > fleet_time: 
                res+=1
                fleet_time = time
                
        return res
            
            