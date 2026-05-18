class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        stop_to_routes = defaultdict(list)
        graph = defaultdict(list)

        for route in range(len(routes)):
            stops = routes[route]
            for stop in stops:
                stop_to_routes[stop].append(route)

        for k, vs in stop_to_routes.items():
            if len(vs) <= 1: continue
            else:
                for i in range(len(vs)):
                    for j in range(i+1, len(vs)):
                        u, v = vs[i], vs[j]
                        graph[u].append(v)
                        graph[v].append(u)

        if source == target: return 0
        src = stop_to_routes[source]
        dest = set(stop_to_routes[target])

        q = deque()
        visited = set()
        for route in stop_to_routes[source]:
            q.append((route, 1))
            visited.add(route)

        while q:
            popped_node, popped_dist = q.popleft()
            if popped_node in dest: return popped_dist

            for nbor in graph[popped_node]:
                if nbor in visited: continue
                visited.add(nbor)
                q.append((nbor, popped_dist + 1))

        return -1




            