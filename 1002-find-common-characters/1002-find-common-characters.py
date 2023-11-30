class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # min(ch count from prev word, ch count from current word)
        counters = [Counter(words[0])]
        commons = set(counters[0].keys())
        res = dict() # ch to int
        res2 = []
        
        for word in words[1:]:
            counters.append(Counter(word))
        
        for cnt in counters:
            commons = commons.intersection(set(cnt.keys()))
            
        for com in commons:
            for cnt in counters:
                if com not in res:
                    res[com] = cnt[com]
                else:
                    res[com] = (min(cnt[com], res[com]))
        
        for k,v in res.items():
            res2+=([k] * v)
        
        return res2