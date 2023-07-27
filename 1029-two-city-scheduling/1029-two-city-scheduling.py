class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # first sort based on lowest cost for city A
        # then break ties by highest cost for city B
        # [[10,20],[30,200],[400,50],[30,20]] ==> [[10,20],[30,200],[400,50],[30,20]]
        
        costs.sort(key = lambda x : x[0] - x[1])
        
        n = len(costs)
        res = 0
        for i in range(n//2):
            res+=costs[i][0]
        
        for i in range(n//2, n):
            res+=costs[i][1]
        
        return res
            
