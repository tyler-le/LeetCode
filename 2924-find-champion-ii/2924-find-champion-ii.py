class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # build a graph
        # return the node with no in degree
        
        in_degree = defaultdict(int)
        res = []
        
        for strong, weak in edges:
            in_degree[weak]+=1
        
        for node in range(n):
            if not in_degree[node]:
                res.append(node)
            
        return res[0] if len(res) == 1 else -1
            
        
        