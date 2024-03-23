class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # x + (x-1) + (x+1) = num
        # x + x - 1 + x + 1 = num
        # 3x = num
        # x = num // 3
        
        mid = num // 3
        prev = mid - 1
        nxt = mid + 1
        
        return [prev, mid, nxt] if prev + mid + nxt == num else []