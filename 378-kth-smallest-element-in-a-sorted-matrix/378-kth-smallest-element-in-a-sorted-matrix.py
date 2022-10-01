class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        '''
        Intuition: Treat each list separately and have n pointers to the start of each list (this will be emulated through a heap). Since the top of the min-heap will point to the smallest value, we can pop it and push the next value in that specific list. After doing this k times, we will have found the answer.
        '''
        
        min_heap = []
        n = len(matrix)
        for row in range(n):
            min_heap.append((matrix[row][0], row, 0))
        
        # technically don't need to heapify since sorted
        # heapify(min_heap) 
            
        # pop the k-1 smallest elements and 'increment pointers'
        for i in range(k-1):
            val, r, c = heappop(min_heap)
            if c+1 < n:
                heappush(min_heap, (matrix[r][c+1], r, c+1))
        # the kth smallest is now at the top
        return min_heap[0][0]