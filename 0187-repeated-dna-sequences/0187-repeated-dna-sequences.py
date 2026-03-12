class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        n = len(s)
        window = deque()
        seen = set()
        res = []
        
        for r in range(n):
            window.append(s[r])
            
            while r-l+1 > 10:
                window.popleft()
                l+=1
            
            if r-l+1 == 10 and "".join(window) in seen:
                res.append("".join(window))
            
            seen.add("".join(window))
            
        return list(set(res))
    
