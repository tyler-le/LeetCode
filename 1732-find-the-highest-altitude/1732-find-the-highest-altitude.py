class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        res = -float("inf")
        
        for delta in gain:
            alt+=delta
            res = max(res, alt)
        
        return max(res, 0)