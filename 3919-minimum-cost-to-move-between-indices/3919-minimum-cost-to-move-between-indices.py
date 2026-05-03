class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        closest = [math.inf] * n
        fwd = [0] * n
        back = [0] * n

        for i in range(n):
            if i == 0: 
                closest[i] = 1

            elif i == n-1: 
                closest[i] = i-1
            else: 
                prev = nums[i-1]
                curr = nums[i]
                after = nums[i+1]

                if abs(prev - curr) <= abs(after - curr): closest[i] = i-1
                else: closest[i] = i+1
        
        acc = 0
        for i in range(1, n):
            if closest[i-1] == i: acc+=1
            else: acc+=nums[i] - nums[i-1]
            fwd[i] = acc
        
        acc = 0
        for i in range(n-2, -1, -1):
            if closest[i+1] == i: acc+=1
            else: acc+= nums[i+1] - nums[i]
            back[i] = acc
    
        res = []

        for x, y in queries:
            if x < y:
                res.append(fwd[y] - fwd[x])
            else:
                res.append(back[y] - back[x])
        
        return res

