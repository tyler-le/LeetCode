class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # for each contiguous group of colors, we need to remove all except one
        # we will choose to keep the most time consuming one for optimality reasons
        # hence cost = sum(group) - max(group)
        
        l, r, n = 0, 0, len(colors)
        res = 0
        
        while l < n and r < n:
            
            group_max = 0
            group_sum = 0
            while l < n and r < n and colors[r] == colors[l]: 
                group_max = max(group_max, neededTime[r])
                group_sum+=neededTime[r]
                r+=1
                
            res+=(group_sum - group_max)
            l = r
        
        return res