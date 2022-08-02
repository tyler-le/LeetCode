class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        val = image[sr][sc]
        
        def dfs(i, j, val):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) \
                or image[i][j] != val or image[i][j] == color: 
                return
            
            image[i][j] = color
            
            dfs(i-1, j, val)
            dfs(i+1, j, val)
            dfs(i, j-1, val)
            dfs(i, j+1, val)

        dfs(sr, sc, val)
        return image