class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # (u -> v) if u trusts v

        # find the one with no outgoing edges AND n-1 incoming edges

        indegrees = defaultdict(int)
        outdegrees = defaultdict(int)
        
        for u, v in trust:
            indegrees[v]+=1
            outdegrees[u]+=1
        
        for person in range(1, n+1):
            if indegrees[person] == n-1 and outdegrees[person] == 0:
                return person
        
        return -1