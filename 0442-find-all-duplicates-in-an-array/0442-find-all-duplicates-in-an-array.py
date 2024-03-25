class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        
        return [x for x, y in cnt.items() if y > 1]