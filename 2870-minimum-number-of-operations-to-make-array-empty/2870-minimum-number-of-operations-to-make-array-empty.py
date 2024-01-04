class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
    
        for x, cnt in counts.items():
            if cnt == 1: return -1
            res+=ceil(cnt / 3)
            
        return res