class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_cnt = 0
        
        for row in bank:        
            cnt = row.count("1")
            
            if cnt:
                res+=(prev_cnt * cnt)
                prev_cnt = cnt
            
        return res
            
            
                