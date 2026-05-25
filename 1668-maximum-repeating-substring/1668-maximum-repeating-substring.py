class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence) // len(word)

        for multiplier in range(n, -1, -1):
            if word * multiplier in sequence:
                return multiplier