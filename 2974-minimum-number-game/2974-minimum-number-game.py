class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # alice pops
        # bob pops
        # bob appends
        # alice appends
        
        n = len(nums)
        res = []
        heapify(nums)
        
        while nums:
            alice, bob = heappop(nums), heappop(nums)
            res.append(bob)
            res.append(alice)
        
        return res