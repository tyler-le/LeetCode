class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        min_heap = []
        n = len(matrix)
        for row in range(n):
            min_heap.append((matrix[row][0], row, 0))
        #heapify(min_heap)
        
        while k:
            val, r, c = heappop(min_heap)
            if c+1 < n:
                heappush(min_heap, (matrix[r][c+1], r, c+1))
            k-=1
       
        return val