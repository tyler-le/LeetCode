class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0 for _ in range(len(temperatures))]
        
        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    popped_temp, popped_index = stack.pop()
                    res[popped_index] = i - popped_index
            stack.append((temp, i))
        
        return res
                
        
        
        
        
         
        