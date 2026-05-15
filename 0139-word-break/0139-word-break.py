class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def f(index):
            if index <= 0: return True

            for word in wordDict:
                k = len(word)
                if s[index - k : index] == word:
                    if f(index - k): return True

            return False
            

        n = len(s)
        return f(n)