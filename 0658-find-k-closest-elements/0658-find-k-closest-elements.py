class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = [] 
        res = []
        
        for num in arr:
            diff = abs(x-num)
            
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-diff, num))
            
            elif diff < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-diff, num))
        
                        
        for _, val in max_heap:
            res.append(val)
        res.sort()
        return res
                
            