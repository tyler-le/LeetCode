class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        # f(i) = max repeating substring that STARTS at index i
        n = len(sequence)
        m = len(word)
        res = 0

        @cache
        def f(i):
            if i >= n: return 0
            if sequence[i : i + m] == word: return 1 + f(i + m)
            else: return 0
            
        for x in range(n):
            res = max(res, f(x))

        return res

