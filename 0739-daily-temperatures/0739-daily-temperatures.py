class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = [(temperatures[0], 0)]
        res = [0 for _ in range(n)]

        for i in range(1, n):
        
            curr_temp, curr_index = temperatures[i], i
            
            while stack and curr_temp > stack[-1][0]:
                popped_temp, popped_index = stack.pop()
                res[popped_index] = curr_index - popped_index

            stack.append((curr_temp, curr_index)) 

        return res
