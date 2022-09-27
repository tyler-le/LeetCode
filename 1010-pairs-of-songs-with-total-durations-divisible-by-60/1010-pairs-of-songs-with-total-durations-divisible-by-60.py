class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        res = 0
        hmap = collections.defaultdict(int)
        #each elem % 60 == 0 or 60
        # for t in time:
        #     hmap[t % 60] = t
            
        for t in time:
            if t % 60 == 0:
                res+=hmap[0]
            else:
                res+=hmap[60 - t % 60]
                
            hmap[t % 60]+=1
            
        return res
                