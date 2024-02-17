class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # remove highest frequency until length becomes < half 
        
        n = len(arr)
        min_heap = [-freq for freq in list(Counter(arr).values())]
        
        heapify(min_heap)
        removed = 0
        res = 0
        
        while removed < (n // 2):
            removed+= (-heappop(min_heap))
            res+=1
        
        
        return res