class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = set()

        def backtrack(i, sublist):
            nonlocal res, visited

            if len(sublist) == len(nums):
                res.append(sublist.copy())
                return
            
            for x in nums: 
                if x in visited: continue

                sublist.append(x)
                visited.add(x)

                backtrack(i+1, sublist)

                sublist.pop()
                visited.remove(x)
            
        backtrack(0, [])
        return res
