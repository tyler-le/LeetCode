class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        
        # width of sliding window
        for length in range(len(str(low)), len(str(high)) + 1):
            
            # starting position of sliding window
            for i in range(10-length):
                num = int(s[i:i+length])
                if low <= num <= high:
                    res.append(num)
        return res
                
