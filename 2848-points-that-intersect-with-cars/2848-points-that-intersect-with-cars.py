class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        mini, maxi = float("inf"), -float("inf")
        
        for start, end in nums:
            mini = min(mini, start)
            maxi = max(maxi, end)
            
        arr = [0 for _ in range(101)]
        
        for start, end in nums:
            for i in range(start, end+1):
                arr[i] = 1
        
        return sum(arr)
            
        