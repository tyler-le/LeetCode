class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        res = []

        for word in arr:
            if word == '': continue
            res.append(word)
        
        res.reverse()
        return " ".join(res)
            