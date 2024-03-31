class Solution:
    def modifyString(self, s: str) -> str:
        
        def replace_char(i):
            
            for c in ascii_lowercase:
                valid = True
                
                if i >= 0 and s[i-1] == c: valid = False
                if i+1 < n and s[i+1] == c: valid = False
                    
                if valid: return c
        
        n = len(s)
        s = list(s)
        
        for i in range(n):
    
            if s[i] == "?": 
                s[i] = replace_char(i)
        
        return "".join(s)
                
            