class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        adjacency_list = collections.defaultdict(list)
        
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        visited = set()
        
        def dfs(i, prev):
            if i in visited: return False
            visited.add(i)
            
            for neighbor in adjacency_list[i]:
                if neighbor != prev and not dfs(neighbor, i): 
                    return False
                
            return True
        
        
        return dfs(0, 0) and len(visited) == n