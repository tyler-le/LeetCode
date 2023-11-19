class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while True:
            sumi = numbers[l] + numbers[r]
            
            if sumi == target: return [l+1, r+1]
            elif sumi < target: l+=1
            else: r-=1
                