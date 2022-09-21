class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tups = []
        res = ""
    
        # make (index, ch) pairs and then sort
        tups = sorted([(index, ch) for index, ch in zip(indices, s)])
            
        # since the indices are in order now, we can build the string
        for _, ch in tups:
            res+=ch
            
        return res
            
            