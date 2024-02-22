class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outcoming = defaultdict(int)
        
        for u, v in trust:
            incoming[v]+=1
            outcoming[u]+=1
        
        for i in range(1, n+1):
            if incoming[i] == n-1 and outcoming[i] == 0: return i
        
        return -1