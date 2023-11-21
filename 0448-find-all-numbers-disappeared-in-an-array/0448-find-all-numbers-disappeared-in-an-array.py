class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        arr, res = [0 for _ in range(n+1)], []
        
        for num in nums: arr[num] = 1
                
        for i in range(1, len(arr)):
            if not arr[i]: res.append(i)
                
        return res
        
        