class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, bigger, equal = [], [], []
        
        for num in nums:
            if num < pivot: smaller.append(num)
            elif num > pivot: bigger.append(num)
            else: equal.append(num)
                
        return smaller + equal + bigger