class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(course, visited):
            if course in visited: return False
            
            neighbors = adjacency_list[course]
            visited.add(course)
            
            for nbor in neighbors:
                if not dfs(nbor, visited): return False
                
            adjacency_list[course] = []
            visited.remove(course)
            
            return True
                
       
        adjacency_list = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
        
        for i in range(numCourses):
            visited = set()
            if not dfs(i, visited): return False
            
        return True