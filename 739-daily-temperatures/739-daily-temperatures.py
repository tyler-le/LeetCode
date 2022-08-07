class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res, stack, TEMP = [0 for _ in temperatures], [], 0
       
        for index, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][TEMP]:
                top_temp, top_index = stack.pop()
                res[top_index] = index - top_index
            stack.append((temp, index))
            
        return res