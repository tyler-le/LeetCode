class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = {arr[0] : 1} # map num : result 
        
        for num in arr[1:]:
            if num - difference in cache:
                cache[num] = cache[num-difference] + 1
            else: cache[num] = 1
        
        return max(cache.values())
            
            