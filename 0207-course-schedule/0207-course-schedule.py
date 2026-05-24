class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()


        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u]+=1

        for i in range(numCourses):
            if not indegrees[i]: 
                q.append(i)

        while q:
            popped = q.popleft()
            if popped in visited: return False
            visited.add(popped)

            for nbor in graph[popped]:
                indegrees[nbor]-=1
                if not indegrees[nbor]: 
                    q.append(nbor)

        return len(visited) == numCourses


        