class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        """
        DP
        dp[i] = is s[0...index] word-breakable
        """
        n = len(s)
        dp = [False for _ in range(n)]
        for i in range(n):
            for word in wordDict:
                k = len(word)

                if i-k+1 >=0 and s[i-k+1:i+1] == word:
                    print(word)
                    if i-k+1 == 0: dp[i] = True
                    else: dp[i] |= dp[i-k]

        print(dp)
        return dp[-1]
                    

        """
        Recursive
        f(index) = is s[0...index] word-breakable
        """
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