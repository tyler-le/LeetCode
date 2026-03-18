class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []  
        backlog = []
        times = defaultdict(int)
        min_id, max_id = 0, 0

        for log in logs:
            function_id, category, time = log.split(":")
            max_id = max(max_id, int(function_id))
            time = int(time)

            if category == "start":
                if not stack: 
                    stack.append((function_id, time))
                else:
                    popped_id, popped_time = stack.pop()
                    times[popped_id]+=(time - popped_time)
                    backlog.append(popped_id)
                    stack.append((function_id, time))
            
            else:
                popped_id, popped_time = stack.pop()
                times[popped_id]+=(time - popped_time + 1)
                if not stack and backlog:
                    backlogged_item = backlog.pop()
                    stack.append((backlogged_item, time + 1))

        res = [0 for _ in range(min_id, max_id + 1)]

        for i in range(min_id, max_id + 1):
            res[i] = times[str(i)]
        
        return res

