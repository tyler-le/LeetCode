class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tups = []
        res = ""
        
        for index, ch in zip(indices, s):
            tups.append((index,ch))
            
        tups.sort()
        
        for _, ch in tups:
            res+=ch
        return res
            
            