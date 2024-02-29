class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        total_windows = len(s) - k + 1
        
        return (2**total_windows) % (10**9 + 7)