class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n: return True
        for i, flower in enumerate(flowerbed):
            before = flowerbed[i-1] if i-1 >= 0 else 0
            after = flowerbed[i+1] if i+1 < len(flowerbed) else 0

            can_place = before == 0 and after == 0 and flowerbed[i] == 0

            if can_place:
                flowerbed[i] = 1
                n-=1
  
            # evaluate n
            if not n: 
                return True
        
        return False