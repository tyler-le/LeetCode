class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = Counter(arr)
        n = len(arr)
        
        for num in arr:
            if (counts[num] / n) > .25:
                return num
        