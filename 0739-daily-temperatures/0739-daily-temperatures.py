class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0 for _ in range(n)]
        
        for i in range(n):
            curr = temperatures[i]
            if not stack: 
                stack.append((curr, i))
                
            else:
                top_val, top_index = stack[-1]    
                while stack and curr > top_val:
                    res[top_index] = i - top_index
                    stack.pop()
                    if stack: top_val, top_index = stack[-1]    
                    
                stack.append((curr, i))
                
        return res