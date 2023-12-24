class Solution:
    def minOperations(self, s: str) -> int:
        c1 = c2 = 0
        
        # 0 1 0 1 ...
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1": c1+=1
            elif i % 2 == 1 and s[i] == "0": c1+=1                
            
        # 1 0 1 0 ...
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "0": c2+=1
            elif i % 2 == 1 and s[i] == "1": c2+=1
                
        return min(c1, c2)
                        
            