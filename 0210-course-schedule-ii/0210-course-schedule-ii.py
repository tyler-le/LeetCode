class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        res = []
        visited = set()

        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u]+=1

        for i in range(numCourses):
            if not indegrees[i]:
                q.append(i)
                visited.add(i)

        while q:
            popped = q.popleft()
            res.append(popped)
            for nbor in graph[popped]:
                if nbor in visited: continue
                indegrees[nbor]-=1
                if not indegrees[nbor]:

                    visited.add(nbor)
                    q.append(nbor)
        return res if len(visited) == numCourses else []
                
