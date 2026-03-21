class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        """
        DP SOLUTION
        """
        dp = [
            [1]
        ]

        for i in range(1, numRows):
            prev_res = dp[i-1]
            sublist = [1]

            for j in range(len(prev_res) - 1):
                sublist.append(prev_res[j] + prev_res[j+1])
            
            sublist.append(1)
            dp.append(sublist)

        return dp


        """
        RECURSIVE SOLUTION
        """
        # res = []

        # def f(i):
        #     nonlocal res

        #     sublist = [1]
        #     if i == 1: 
        #         res.append(sublist)
        #         return sublist

        #     prev_res = f(i-1)

        #     for x in range(len(prev_res) - 1):
        #         sublist.append(prev_res[x] + prev_res[x+1])
            
        #     sublist.append(1)
        #     res.append(sublist)
        #     return sublist
        
        # f(numRows)
        # return res
