class Solution:
    def minOperations(self, s: str) -> int:
        res = float("inf")
        
        # 0 1 0 1 ...
        cnt = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1":
                cnt+=1
            elif i % 2 == 1 and s[i] == "0":
                cnt+=1
                
        print(cnt)    
        res = min(cnt, res)
            
        # 1 0 1 0 ...
        cnt = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "0":
                cnt+=1
            elif i % 2 == 1 and s[i] == "1":
                cnt+=1
                
        res = min(cnt, res)
            
        return res
            
            