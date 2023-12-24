class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        
        seen = set(count.values())
        
        return len(seen) == len(count.values())