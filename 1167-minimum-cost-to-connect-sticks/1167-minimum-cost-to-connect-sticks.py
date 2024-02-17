class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # min heap to combine sticks
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first, second = heappop(sticks), heappop(sticks)
            heappush(sticks, first+second)
            cost+=(first+second)
            
        return cost