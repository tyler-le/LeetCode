class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # to be valid, their remainders have to add up to 60 or to 0
        
        # map remainder to number of times it happens
        hmap = collections.defaultdict(int) 
        res = 0
        
        for t in time:
            remainder = t % 60
            
            if remainder == 0: res+=hmap[0]
            else: res+=hmap[60 - remainder]
            
            hmap[remainder]+=1
            
        return res
            