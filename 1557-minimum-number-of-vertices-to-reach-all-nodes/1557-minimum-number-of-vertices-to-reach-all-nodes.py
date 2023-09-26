class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # map node to incoming edges
        hmap = defaultdict(int)
        
        for u, _ in edges:
            hmap[u] = 0
                
        for _, v in edges:
            hmap[v]+=1
        
        return [node for node, incoming in hmap.items() if incoming == 0]
        