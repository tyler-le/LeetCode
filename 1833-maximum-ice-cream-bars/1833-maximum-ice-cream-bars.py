class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res, curr = 0, 0
        
        for cost in costs:
            if coins - cost >= 0:
                res+=1
                coins-=cost
            else:
                return res
        
        return res