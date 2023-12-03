class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(word):
            l, r = 0, len(word)-1
            
            while l < r:
                if word[l] == word[r]:
                    l+=1
                    r-=1
                else:
                    return False
            
            return True
        
        for word in words:
            if is_palindrome(word):
                return word
        
        return ""