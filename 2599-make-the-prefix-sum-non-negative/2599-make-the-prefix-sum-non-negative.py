class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        min_heap = []
        curr = 0
        res = 0
        
        for num in nums:
            curr+=num
            heappush(min_heap, num)
            if curr < 0:
                res+=1
                curr-=heappop(min_heap)
                
        return res