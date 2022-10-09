class Solution:
    def numberOfWays(self, s: str) -> int:
        # map all possible combinations to their count
        # 0, 1, 01, 10, 010, 101, 110, 011, 000, 111
        count = collections.defaultdict(int)
        # 101 or 010
        
        for digit in s:
            if digit == "0":
                count["0"]+=1
                count["10"]+=count["1"]
                count["010"]+=count["01"]
                
                
            elif digit =="1":
                count["1"]+=1
                count["01"]+=count["0"]
                count["101"]+=count["10"]
                
        return count["101"] + count["010"]