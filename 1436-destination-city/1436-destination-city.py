class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = collections.defaultdict(list)
        cities = set()
        for src, dest in paths:
            cities.add(src)
            cities.add(dest)
            graph[src].append(dest)
        
        for city in cities:
            if not graph[city]: return city
            