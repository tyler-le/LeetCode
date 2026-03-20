class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)

        x = n // m

        for i in range(x, -1, -1):
            if word*i in sequence: return i
        return 0
    