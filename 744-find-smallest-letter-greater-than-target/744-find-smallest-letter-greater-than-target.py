class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target > letters[len(letters) - 1] or target < letters[0]:
            return letters[0]
        
        low, high = 0, len(letters) - 1
        index = 0
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                index = mid
                high = mid - 1
                
            else:
                low = mid + 1
            
        return letters[index]
        