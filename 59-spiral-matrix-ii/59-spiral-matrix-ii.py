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
        
        while curr_num <= n*n:
            # go left to right
            for col in range(left, right+1):
                #if curr_num > n**2: return res
                res[top][col] = curr_num
                curr_num+=1
                
            # go down
            for row in range(top+1, bottom+1):
                #if curr_num > n**2: return res
                res[row][right] = curr_num
                curr_num+=1
                
                
            # go right to left
            if top != bottom:
                for col in range(right-1, left-1, -1):
                    #if curr_num > n**2: return res
                    res[bottom][col] = curr_num
                    curr_num+=1
            
            # go up
            if left != right:
                for row in range(bottom-1, top, -1):
                    #if curr_num > n**2: return res
                    res[row][left] = curr_num
                    curr_num+=1
            
            left+=1
            right-=1
            top+=1
            bottom-=1
            
        return res
            