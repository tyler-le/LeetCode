class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hmap = collections.defaultdict(int)
        
        for u,v in edges:
            hmap[u]+=1
            hmap[v]+=1
            
            if hmap[u] > 1:
                return u
            if hmap[v] > 1:
                return v
    
        