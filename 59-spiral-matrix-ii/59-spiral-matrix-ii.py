class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        curr_num = 1
        num_iters = 0
        
        while curr_num <= n**2:
            
            # go left to right
            for col in range(left, right+1):
                res[top][col] = curr_num
                curr_num+=1
                
            # go up to down
            for row in range(top+1, bottom+1):
                res[row][right] = curr_num
                curr_num+=1
                
                
            # go right to left
            if top != bottom:
                for col in range(right-1, left-1, -1):
                    res[bottom][col] = curr_num
                    curr_num+=1
            
            # go down to up
            if left != right:
                for row in range(bottom-1, top, -1):
                    res[row][left] = curr_num
                    curr_num+=1
            
            left+=1
            right-=1
            top+=1
            bottom-=1
            
        return res
            