class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 0
        hmap = collections.defaultdict(int)
        
        for t in text: hmap[t]+=1
            
        while True:
            for ch in "balloon":
                if hmap[ch] == 0: return res
                hmap[ch]-=1
            res+=1
            
        