class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # map position to number of gaps
        hmap = defaultdict(int)
        
        for w in wall:
            pos = 0
            for x in w[:-1]:
                pos+=x
                if pos == sum(w): continue
                hmap[pos]+=1
        
        if not hmap: return len(wall)
        return len(wall) - max(hmap.values())