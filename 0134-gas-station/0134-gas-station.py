class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # loop thru each gas station and see if you can do a circuit
        
        # need to keep track of curr. if curr < cost[i] at any point,  
        # then we should move onto the next gas station
        
        # else, we have enough gas. subtract cost[i] and add in cost[i+1]
        
        n = len(gas)
        total = start = tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            # check next station
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1