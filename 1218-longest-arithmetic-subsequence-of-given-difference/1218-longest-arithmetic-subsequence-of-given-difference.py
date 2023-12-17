class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = collections.defaultdict(int)
        cache[arr[0]] = 1 # map num : result 
        
        for num in arr[1:]:
            cache[num] = max(cache[num-difference] + 1, 1)
            
        
        return max(cache.values())
            
            