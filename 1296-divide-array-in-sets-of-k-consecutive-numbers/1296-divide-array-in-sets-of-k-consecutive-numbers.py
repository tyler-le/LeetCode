class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        cnt = Counter(nums)
        nums.sort()
        
        for num in nums:
            if not cnt[num]: continue
                
            for i in range(k):
                x = num + i
                
                if x not in cnt: 
                    return False
                cnt[x]-=1
                if not cnt[x]: del cnt[x]
        
        return True
        