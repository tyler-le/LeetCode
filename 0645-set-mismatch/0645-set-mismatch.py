class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        
        res = [-1, -1]
        n = len(nums)
                
        for i in range(1,n+1):
            if cnt[i] == 2:
                res[0] = i
            elif cnt[i] == 0: 
                res[1] = i
            
        return res