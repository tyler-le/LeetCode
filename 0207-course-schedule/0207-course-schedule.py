class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(course):
            if course in visited: return False
            if graph[course] == []: return True
            
            visited.add(course)
            
            for nbor in graph[course]: 
                if not dfs(nbor):
                    return False
                
            visited.remove(course)
            
            graph[course] = []
            
            return True
            
                
        graph = defaultdict(list)
        visited = set()
        num_visited = 0
        
        for u, v in prerequisites:            
            graph[v].append(u)
            
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True
            
            
        