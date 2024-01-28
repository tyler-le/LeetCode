class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        res = []
        graph = defaultdict(list)
        
        for process, parent in zip(pid, ppid):
            graph[parent].append(process)
            
        def dfs(node):
            nonlocal res
            res.append(node)
            
            for child in graph[node]:
                dfs(child)
                
            
        dfs(kill)
        return res
            
            