class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # map width - to - height : count
        hmap = defaultdict(int)
        res = 0
        for width, height in rectangles:
            res+=hmap[width / height]
            hmap[width / height]+=1
        
        return res
            