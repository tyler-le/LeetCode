class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        
        hmap1, hmap2 = defaultdict(int), defaultdict(int)
        res = set()
        
        for word in s1: hmap1[word]+=1        
        for word in s2: hmap2[word]+=1
            
        for word, cnt in hmap1.items():
            if cnt == 1 and word not in hmap2:
                res.add(word)
                
        for word, cnt in hmap2.items():
            if cnt == 1 and word not in hmap1:
                res.add(word)
                
        return res
       