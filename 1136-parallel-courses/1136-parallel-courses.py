class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        # topological sort
        
        res = 0
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        q = deque()
        num_visited = 0
        
        for prev_course, next_course in relations:      
            graph[prev_course].append(next_course)
            indegrees[next_course]+=1
            
        for i in range(1, n+1):
            if not indegrees[i]: 
                q.append((i, 1))
        
        while q:
            popped_course, popped_semester = q.popleft()
            num_visited+=1
            res = max(res, popped_semester)
            
            for nbor in graph[popped_course]:
                indegrees[nbor]-=1
                if not indegrees[nbor]:
                    q.append((nbor, popped_semester+1))
            
        
        return res if (num_visited == n) else -1
        
        