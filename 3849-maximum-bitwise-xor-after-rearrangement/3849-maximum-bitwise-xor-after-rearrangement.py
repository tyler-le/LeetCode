class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        num_ones_in_t = t.count("1")
        s = list(s)
        t = ['0' for _ in range(len(t))]

        def get_result(x, y):
            res = []
            
            for dx, dy in zip(x,y):
                if dx == "1" and dy == "1":
                    res.append("0")
                elif dx == "0" and dy == "0":
                    res.append("0")
                else:
                    res.append("1")

            return "".join(res)

        # first pass - put all the 1's in the 0 positions
        for i in range(len(s)):
            if not num_ones_in_t: 
                break
                
            if s[i] == "0":
                t[i] = "1"
                num_ones_in_t-=1
                
                

        for i in range(len(t) - 1, -1, -1):
            if t[i] == '0' and num_ones_in_t:
                t[i] = '1'
                
                num_ones_in_t-=1
            if not num_ones_in_t:
                break
        
                
        return get_result("".join(s), "".join(t))
        