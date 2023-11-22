class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort()
        curr_p, curr_s = cars.pop()
        bottleneck = (target - curr_p) / (curr_s)
        res = 1
        
        while cars:
            curr_p, curr_s = cars.pop()
            curr_time = (target - curr_p) / (curr_s)
            
            if bottleneck < curr_time:
                res+=1
                bottleneck = curr_time
                
        return res