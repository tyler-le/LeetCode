class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        
        
        while students:
            n = len(students)
            cnt = 0
            while students[0] != sandwiches[0]:
                if cnt == n: 
                    return n
                cnt+=1
                students.append(students.popleft())
            
            sandwiches.popleft()
            students.popleft()
        
        return 0
            