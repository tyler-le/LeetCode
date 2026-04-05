class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        visited = set()
        res = []

        for dst, src in prerequisites:
            graph[src].append(dst)
            indegrees[dst]+=1
        
        for crs in range(numCourses):
            if not indegrees[crs]:
                q.append(crs)

        while q:
            popped = q.popleft()
            res.append(popped)
            visited.add(popped)

            for nbor in graph[popped]:
                if nbor in visited: continue
                indegrees[nbor]-=1
                if not indegrees[nbor]:
                    q.append(nbor)

        return res if len(visited) == numCourses else []


