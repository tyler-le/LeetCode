class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        # f(i) = max repeating substring that ENDS at index i
        n = len(sequence)
        m = len(word)
        res = 0

        @cache
        def f(i):
            if i < 0: return 0

            if sequence[i - m + 1 : i + 1] == word:
                return 1 + f(i - m)
            else:
                return 0

            
        for x in range(n-1, -1, -1):
            res = max(res, f(x))

        return res

