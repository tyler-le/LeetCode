class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []  
        times = defaultdict(int)
        max_id = 0

        for log in logs:
            function_id, category, time = log.split(":")
            max_id = max(max_id, int(function_id))
            time = int(time)

            if category == "start":
                if not stack: 
                    stack.append((function_id, time))
                else:
                    top_fxn, top_time = stack[-1]
                    times[top_fxn]+=(time - top_time)
                    stack.append((function_id, time))
            
            else:
                popped_fxn, popped_time = stack.pop()
                times[popped_fxn] += (time - popped_time + 1)
                if stack: stack[-1] = (stack[-1][0], time + 1) 
                

        res = []

        for i in range(max_id+1):
            res.append(times[str(i)])
        
        return res

