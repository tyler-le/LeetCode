class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        values = set()
        for key, value in count.items():
            if value in values: return False
            values.add(value)
        return True