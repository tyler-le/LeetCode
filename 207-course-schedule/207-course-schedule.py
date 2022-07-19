class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create an empty prereqlist for each course
        prereq_map = { i:[] for i in range(numCourses)} 
        
        # map each course to prereq list
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        # needed for backtracking
        visited = set()
        
        def dfs(course):
            # if already visited, we are in a loop
            if course in visited:
                return False
            
            # if course has no prereqs, we hit a base case and return True
            if prereq_map[course] == []:
                return True
            
            visited.add(course)
            
            # for each prereq in our course list, run dfs on it
            for prereq in prereq_map[course]:
                if not dfs(prereq): return False
                
            # unvisit current course    
            visited.remove(course)
            
            # going this far means the course can be taken. to speed up future calculations, we               just set prereqs to [] to immediately get to base case
            prereq_map[course] = []
            return True
        
        # we need the for loop in the case of an unconnected graph
        for i in range(numCourses):
            if not dfs(i): return False
        return True


