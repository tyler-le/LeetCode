class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # initialize vars
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()
        res = []
        
        # convert to adjacency matrix
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u]+=1
                    
        # add all source nodes to queue
        for crs in range(numCourses):
            if indegrees[crs] == 0: 
                q.append(crs)
        
        # for each outgoing edge from source node u -> v, decrement indegree[v]
        while q:
            popped = q.popleft()
            visited.add(popped)
            res.append(popped)
            
            for nbor in graph[popped]:
                if nbor in visited: continue
                indegrees[nbor]-=1
                if indegrees[nbor] == 0:
                    q.append(nbor)
                    
        
        return res if len(visited) == numCourses else []