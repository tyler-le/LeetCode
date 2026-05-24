class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        # f(i) = longest subsequence ending at index i
        
        cache = defaultdict(int)

        for x in arr:
            cache[x] = 1 + cache[x - difference]

        return max(cache.values())