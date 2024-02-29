class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        total_windows = 0
        
        for i in range(len(s) - k + 1):
            total_windows+=1
        
        return (2**total_windows) % (10**9 + 7)