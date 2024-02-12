class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        min_heap, res = [], []
        time, task_index, n = tasks[0][0], 0, len(tasks)

        while len(res) < n:
            
            # add 0 or more things to the heap
            while (task_index < n) and (tasks[task_index][0] <= time):
                heappush(min_heap, (tasks[task_index][1], tasks[task_index][2]))
                task_index+=1
            
        
            # if heap has items -> pop it and advance current time
            if min_heap:
                task_time, original_index = heappop(min_heap)
                time+=task_time
                res.append(original_index)
                
            # else no things in heap -> fast forward time if possible
            elif task_index < n:
                time = tasks[task_index][0]
        
        return res
        
        
                