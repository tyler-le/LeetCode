class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment = 1

        for ch in s:
            if ch == "0": segment = 0
            if not segment and ch == "1": return False
        
        return True