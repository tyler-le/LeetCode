class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        # map position : number of gaps
        count = defaultdict(int)
        
        for w in wall:
            curr = 0
            for x in w[:-1]:
                curr+=x
                count[curr]+=1
        if not count: return len(wall)
        return len(wall) - max(count.values())
        
        