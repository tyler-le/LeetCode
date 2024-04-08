class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while students:
            n = len(students)
            cnt = 0
            
            # keep circulating students if they don't match
            while students[0] != sandwiches[0]:
                if cnt == n: 
                    # we've done a full pass of students and need to exit loop
                    return n
                cnt+=1
                students.append(students.popleft())
            
            # we found a match, so pair the two together
            sandwiches.popleft()
            students.popleft()
        
        return 0
            