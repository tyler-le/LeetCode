class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        
        for num in nums:
            res_len = len(res)
            
            for i in range(res_len):
                new_set = res[i] + [num]
                res.append(new_set)
                       
        return res
                
                