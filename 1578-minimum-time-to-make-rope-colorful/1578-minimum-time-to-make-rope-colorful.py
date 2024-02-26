class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        l, r = 0, 0
        n = len(colors)
        cnt = 0
        
        while l < n and r < n:
            curr_max = neededTime[l]
            
            while r+1 < n and colors[l] == colors[r+1]:
                r+=1
                curr_max = max(curr_max, neededTime[r])
                
            cnt+=curr_max
            
            l = r + 1
            r = l
        
        return sum(neededTime) - cnt
                