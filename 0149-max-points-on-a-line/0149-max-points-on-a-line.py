class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calc_slope(p1, p2):
            x1,y1 = p1
            x2,y2 = p2
            # vertical line case
            if (x2-x1 == 0): return 
            else: return (y2-y1) / (x2-x1)
        
        n = len(points)
        res = 1
        for i in range(n):
            hmap = collections.defaultdict(int)
            for j in range(i+1,n):
                slope = calc_slope(points[i], points[j])
                hmap[slope]+=1
                res = max(res, max(hmap.values())+1)
        return res
        
                
                
                
            