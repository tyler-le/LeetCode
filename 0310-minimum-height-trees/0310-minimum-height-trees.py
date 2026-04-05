class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build the graph and for every vertex, mark that as root and find height

        graph = defaultdict(list)
        res = []
        indegrees = defaultdict(int)
        q = deque()

       
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegrees[u]+=1
            indegrees[v]+=1
        
        for node in range(n):
            if indegrees[node] == 1:
                q.append(node)
        
        visited = set(list(q))

        while len(q) > 2:
            level_size = len(q)
            for _ in range(level_size):
                popped = q.popleft()

                for nbor in graph[popped]:
                    indegrees[nbor]-=1
                    if indegrees[nbor] == 1:
                        q.append(nbor)
        
        return list(q)

        
        

        

        