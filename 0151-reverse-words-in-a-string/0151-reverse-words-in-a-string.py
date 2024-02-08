class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        l, r = 0, len(s)-1
        res = []
        
        for w in s:
            if w != "":
                res.append(w)
        
        return " ".join(res[::-1])
                