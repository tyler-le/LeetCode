class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        def predicate(word):
            if word == "": return False
            return True
        
        words = s.split(" ")
        words = list(filter(predicate, words))

        return len(words[-1])