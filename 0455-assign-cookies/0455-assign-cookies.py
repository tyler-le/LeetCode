class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        res, s_ptr = 0, 0
        
        g.sort()
        s.sort()

        for greed in g:
            while s_ptr < len(s) and s[s_ptr] < greed: 
                s_ptr+=1
            
            if s_ptr >= len(s): return res
            
            res+=1
            s_ptr+=1
        
        return res
                