class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])

        s = list(s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in vowels: return "".join(s)
            if s[i] in vowels: s[i] = ""

        return "".join(s)