class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        visited = set()
        adjacency_list = collections.defaultdict(list)
        
        for start, end in edges:
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)
            
        def dfs(prev, curr):
            
            if curr in visited: 
                return False
            visited.add(curr)
            for nbor in adjacency_list[curr]:            
                if nbor == prev:
                    continue
                
                res = dfs(curr, nbor)
                if not res: return False
            return True
        
        print(visited)
        return dfs(0, 0) and n == len(visited)
            