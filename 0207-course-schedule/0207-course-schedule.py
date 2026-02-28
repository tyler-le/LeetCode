class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build the graph
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()

        for (u, v) in prerequisites:
            graph[v].append(u)
            indegrees[u]+=1

        for course in range(numCourses):
            if not indegrees[course]: 
                q.append(course)        

        while q:
            popped = q.popleft()
            visited.add(popped)
            
            for nbor in graph[popped]:
                indegrees[nbor]-=1
                if not indegrees[nbor]: 
                    q.append(nbor)
                
        
        return len(visited) == numCourses
        