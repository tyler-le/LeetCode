class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # brute force, do a max of len(s) rotations
        return goal in s+s and len(goal) == len(s)
            