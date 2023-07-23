class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        dp = [[] for _ in range(n+1)]
        
        dp[1] = ["a","e","i","o","u"]
        
        for i in range(2, n+1):
            
            for word in dp[i-1]:
                for vowel in vowels:
                    if word[-1] > vowel: continue
                    new_word = word + vowel
                    dp[i].append(new_word)
       
        return len(dp[-1])