class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # count how many flowers we can place and check if >= n
        
        res = 0
        
        for i in range(len(flowerbed)):
            before = flowerbed[i-1] if i > 0 else 0
            after = flowerbed[i+1] if i+1 < len(flowerbed) else 0
                
            if not before and not after and not flowerbed[i]: 
                flowerbed[i] = 1
                res +=1
        
        return res >= n