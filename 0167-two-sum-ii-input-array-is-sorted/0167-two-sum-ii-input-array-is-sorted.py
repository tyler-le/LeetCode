class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left+=1
            elif numbers[left] + numbers[right] > target:
                right-=1
            else:
                return [left+1, right+1]