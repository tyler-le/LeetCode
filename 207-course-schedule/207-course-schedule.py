class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # dfs
        prereq_map = { i:[] for i in range(numCourses)} 
        
        # map each course to : prereq list
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if prereq_map[course] == []:
                return True
            
            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            prereq_map[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True


