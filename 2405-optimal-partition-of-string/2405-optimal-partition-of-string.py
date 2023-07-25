class Solution:
    def partitionString(self, s: str) -> int:
        res = 1
        visited = set()
        
        for ch in s:
            if ch in visited:
                res+=1
                visited = set()
            visited.add(ch)
            
        return res
        