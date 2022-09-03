class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if edge_map[node] == []: return True
            if node in visited: return False
            
            visited.add(node)
            
            for neighbor in edge_map[node]:
                if not dfs(neighbor): return False
            
            visited.remove(node)
            edge_map[node] = []
            return True
        
        
        edge_map, visited = collections.defaultdict(list), set()
        
        # create adjacency list
        for course, prereq in prerequisites:
            edge_map[course].append(prereq)
            
        # run dfs on each node
        for i in range(0, numCourses):
            if not dfs(i): return False
        return True
        
        
            
        
        