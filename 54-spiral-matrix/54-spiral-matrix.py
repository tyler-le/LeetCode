class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        
        while len(res) < (rows*cols):
            # go right
            for col in range(left, right):
                print("right", [top,col])
                res.append(matrix[top][col])
            
            # go down
            for row in range(top+1, bottom):
                print("down", [row, right-1])
                res.append(matrix[row][right-1])
                
            # go left
            if top != bottom-1:
                for col in range(right-2, left-1, -1):
                    print("left", [bottom-1, col])
                    res.append(matrix[bottom-1][col])
                
            # go up
            if left != right-1:
                for row in range(bottom-2, top, -1):
                    print("up", [row, left])
                    res.append(matrix[row][left])
                    
            left+=1
            right-=1
            top+=1
            bottom-=1
            
        return res
        