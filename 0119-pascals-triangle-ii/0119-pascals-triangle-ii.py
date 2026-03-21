class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        DP SOLUTION
        """
        prev_res = [1]

        for i in range(1, rowIndex + 1):
            sublist = [1]

            for j in range(len(prev_res) - 1):
                sublist.append(prev_res[j] + prev_res[j+1])
            
            sublist.append(1)
            prev_res = sublist

        return prev_res


        # """
        # RECURSIVE SOLUTION
        # """

        # def f(i):

        #     sublist = [1]
        #     if i == 1: return sublist

        #     prev_res = f(i-1)

        #     for x in range(len(prev_res) - 1):
        #         sublist.append(prev_res[x] + prev_res[x+1])
            
        #     sublist.append(1)
        #     return sublist
        
        # return f(rowIndex + 1)
