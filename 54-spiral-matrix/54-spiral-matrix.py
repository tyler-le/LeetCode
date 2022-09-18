class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        top = left = 0
        right = cols - 1
        bottom = rows - 1
        
        while len(res) < rows*cols:
            # go right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            
            
            # go down
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            
            # go left
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            
            # go up
            if left != right:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
                
            left+=1
            right-=1
            top+=1
            bottom-=1
            
        return res
        