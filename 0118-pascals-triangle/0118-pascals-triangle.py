class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        def f(i):
            nonlocal res

            sublist = [1]
            if i == 1: 
                res.append(sublist)
                return sublist

            
            prev_res = f(i-1)

            for x in range(len(prev_res) - 1):
                sublist.append(prev_res[x] + prev_res[x+1])
            
            sublist.append(1)
            res.append(sublist)
            return sublist
        
        f(numRows)
        return res
