class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        acc = 0
        
        for i in range(len(flowerbed)):
            left_empty = (i == 0) or (flowerbed[i-1] == 0)
            right_empty = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
            can_plant = left_empty and right_empty and flowerbed[i] == 0
            
            if can_plant:
                flowerbed[i] = 1
                acc+=1
                if acc >= n: return True
        return acc >= n