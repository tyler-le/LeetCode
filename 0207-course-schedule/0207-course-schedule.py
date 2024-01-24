class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # initialize vars
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()
        
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
            
            for nbor in graph[popped]:
                if nbor in visited: continue
                indegrees[nbor]-=1
                if indegrees[nbor] == 0:
                    q.append(nbor)
                    
        
        return len(visited) == numCourses