class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        counts = []
        res = 0
        
        for i, row in enumerate(bank):
            cnt = row.count("1")
            if cnt: 
                counts.append(cnt)
                        
                if len(counts) >= 2:
                    res+=(counts[-1] * counts[-2])
            
        return res
    
    [1, 1]