class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        res = 0
        hmap = collections.defaultdict(int)
       
        for t in time:
            # look for a remainder s.t. r + (t % 60) == 0
            if t % 60 == 0: res+=hmap[0]
                
            # look for a remainder s.t. r + (t % 60) == 60
            else: res+=hmap[60 - (t % 60)]
              
            hmap[t % 60]+=1
            
        return res
                