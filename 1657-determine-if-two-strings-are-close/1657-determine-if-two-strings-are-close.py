class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2): return False
        
        cnt_a = Counter(word1)
        cnt_b = Counter(word2)
        n = len(word1)

        arr_a = [0 for _ in range(n+1)]
        arr_b = [0 for _ in range(n+1)]

        if cnt_a.keys() != cnt_b.keys(): 
            return False

        for _, freq in cnt_a.items():
            arr_a[freq]+=1
        
        for _, freq in cnt_b.items():
            arr_b[freq]+=1

        return arr_a == arr_b
