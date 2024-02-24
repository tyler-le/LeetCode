class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        # set pointers from right and collect times greedily
        
        
        
        res = 0
        n = len(garbage)
        glass, paper, metal = n-1, n-1, n-1
        
        # set plastic ptr
        while paper >= 0 and "P" not in garbage[paper]: paper-=1
        
        # set glass ptr
        while glass >= 0 and "G" not in garbage[glass]: glass-=1
        
        # set metal ptr
        while metal >= 0 and "M" not in garbage[metal]: metal-=1
            
            
        for i in range(paper+1):
            res+=(garbage[i].count("P") + (travel[i-1] if i-1 >= 0 else 0))
            
        for i in range(glass+1):
            res+=(garbage[i].count("G") + (travel[i-1] if i-1 >= 0 else 0))
            
        for i in range(metal+1):
            res+=(garbage[i].count("M") + (travel[i-1] if i-1 >= 0 else 0))
        
        return res
            
            
            
            
            
            
            
            
            