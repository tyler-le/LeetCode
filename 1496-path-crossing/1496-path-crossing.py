class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        curr = [0,0]
        visited = set([tuple(curr)])
        
        for p in path:
            if p == "N": curr[0]+=1
            elif p == "S": curr[0]-=1
            elif p == "E": curr[1]+=1
            else: curr[1]-=1
            
            if tuple(curr) in visited: return True
            visited.add(tuple(curr))

        return False