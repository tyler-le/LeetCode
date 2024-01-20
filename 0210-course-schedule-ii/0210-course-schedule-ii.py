class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        num_visited = 0
        
        
        # build graph
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
            
        # get all courses with indegree 0
        for i in range (numCourses):
            if not indegree[i]: 
                q.append(i)
                
        while q:
            popped = q.popleft()
            res.append(popped)
            for crs in graph[popped]:
                indegree[crs]-=1
                if not indegree[crs]:
                    q.append(crs)

        return res if len(res) == numCourses else []
            
        