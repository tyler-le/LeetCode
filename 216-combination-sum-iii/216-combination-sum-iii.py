class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(path, next_num):
            
            if sum(path) == n and len(path) == k: 
                res.append(path[::])
                return
            
            if len(path) >= k or sum(path) > n: return
            
            for i in range(next_num, 9):
                path.append(i+1)
                dfs(path, i+1)
                path.pop()
            
                
        dfs([], 0)
        return res
            