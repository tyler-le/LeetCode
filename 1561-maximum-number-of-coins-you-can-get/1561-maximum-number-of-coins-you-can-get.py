class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)
        res = 0
        
        while q: 
            alice = q.pop()
            you = q.pop()
            bob = q.popleft()
            res+=you
        
        return res
            