class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hmap = collections.defaultdict(int)
        
        for u,v in edges:
            hmap[u]+=1
            hmap[v]+=1
        
        for k, v in hmap.items():
            if v == len(edges):
                return k
        