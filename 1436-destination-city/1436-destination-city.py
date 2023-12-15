class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = dict()
        
        for src, dest in paths:
            if src not in graph: graph[src] = [dest]
            else: graph[src].append(dest)
            if dest not in graph: graph[dest] = []
        
        for src, dests in graph.items():
            if not dests: return src
            