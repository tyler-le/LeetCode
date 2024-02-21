class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        commons = [math.inf for _ in range(26)]
        res = ""
        
        for word in words:
            cnt = Counter(word)
            
            for i in range(26):
                commons[i] = min(commons[i], cnt[chr(i + ord('a'))])
            
        for i in range(len(commons)):
            if commons[i]:
                res+=(chr(i + ord('a'))) * commons[i]
        
        return res