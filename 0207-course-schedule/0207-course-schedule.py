class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # convert to graph adjacency list
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        queue = deque()
        
        for curr, pre in prerequisites:
            graph[pre].append(curr) 
            indegree[curr]+=1
        
        # get node with indegree 0, remove its nbors, continue
        nodes_visited = 0
        
        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)
                
        while queue:
            popped = queue.popleft()
            nodes_visited+=1
            
            for nbor in graph[popped]:
                indegree[nbor]-=1
                if not indegree[nbor]:
                    queue.append(nbor)
                    
        return nodes_visited == numCourses
                
