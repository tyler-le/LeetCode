class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degrees = defaultdict(int)
        res = []

        for u, v in edges:
            in_degrees[v]+=1

        for i in range(n):
            if not in_degrees[i]: res.append(i)
        
        if len(res) > 1: return -1
        else: return res[0]
        