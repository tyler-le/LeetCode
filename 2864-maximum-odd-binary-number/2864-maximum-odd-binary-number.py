class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # greedily place all "1" in msb and reserve a spot for the 0th posiiton
        
        ones_freq = s.count("1") - 1
        res = ["0" for _ in range(len(s))]
        
        res[-1] = "1"
        
        for i in range(ones_freq):
            res[i] = "1"
        
        return "".join(res)
        
        