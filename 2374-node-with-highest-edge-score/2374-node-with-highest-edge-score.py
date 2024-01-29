class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        hmap = defaultdict(int)
        n = len(edges)
        res = 0
        max_score = -float("inf")
        
        for i in range(n):
            hmap[edges[i]]+=i
            
        
        for i in range(n):
            if hmap[i] > max_score:
                res = i
                max_score = hmap[i]
        
        return res