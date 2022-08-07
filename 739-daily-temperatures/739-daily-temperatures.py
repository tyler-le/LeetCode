class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in temperatures]
        stack = []
        
        for index, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]:
                top_temp, top_index = stack.pop()
                res[top_index] = index - top_index
            stack.append((temp, index))
            
        return res