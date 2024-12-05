class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumi = sum(apple)
        res = 0
        capacity.sort(reverse=True)
        
        for cap in capacity:
            if sumi <= 0:
                return res
            sumi-=cap
            res+=1
        return res
            
            