class Solution:
    def minimumSteps(self, s: str) -> int:
        # find right most 0 index

        # find left most 1 index

        zeros_seen = 0
        res = 0

        for ch in s[::-1]:
            if ch == "0":
                zeros_seen+=1
            else:
                res+=zeros_seen
        
        return res
