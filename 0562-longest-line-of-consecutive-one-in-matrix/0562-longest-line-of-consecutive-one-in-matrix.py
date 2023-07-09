class Solution(object):

    
    
    
    
    def longestLine(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n,m,res = len(mat), len(mat[0]), 0
        
        def check_right(i,j):
            count = 0
            while j < m and mat[i][j] == 1:
                count+=1
                j+=1
            return count

        def check_down(i,j):
            count = 0
            while i < n and mat[i][j] == 1:
                count+=1
                i+=1
            return count
        
        def check_diag(i,j):
            count = 0
            while i < n and j < m and mat[i][j] == 1:
                count+=1
                i+=1
                j+=1
            return count
        
        def check_antidiag(i,j):
            count = 0
            while 0 <= i < n and 0 <= j < m and mat[i][j] == 1:
                count+=1
                i-=1
                j+=1
            return count
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    res = max(res, 
                              check_right(i,j), 
                              check_down(i,j), 
                              check_diag(i,j),
                              check_antidiag(i,j))
                
        return res