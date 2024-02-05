class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hmap = defaultdict(int)
        l = 0
        n = len(fruits)
        res = 0
        
        for r in range(n):
            hmap[fruits[r]]+=1
            
            while len(hmap) > 2:
                hmap[fruits[l]]-=1
                if not hmap[fruits[l]]: del hmap[fruits[l]]
                l+=1
                    
            res = max(res, r-l+1)
            
        return res