class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = [ch for ch in s]
        t = [ch for ch in t]
        
        def f(chars):
            res = []
            
            for ch in chars:
                if ch != "#":
                    res.append(ch)
                else:
                    if res: res.pop()
                        
            return res
        
        return f(s) == f(t)
                    
                
        
            
        