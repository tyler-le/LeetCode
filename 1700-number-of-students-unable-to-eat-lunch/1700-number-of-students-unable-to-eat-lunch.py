class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        CIRCLE, RECT = 0, 1
        prefers_circle = students.count(CIRCLE)
        prefers_rect = students.count(RECT)
        
        sandwiches = deque(sandwiches)
        
        while sandwiches:
            if sandwiches[0] == CIRCLE:
                if prefers_circle: 
                    prefers_circle-=1
                    sandwiches.popleft()
                else: 
                    return len(sandwiches)
            else:
                if prefers_rect: 
                    prefers_rect-=1
                    sandwiches.popleft()
                else: 
                    return len(sandwiches)
        
        return 0
                