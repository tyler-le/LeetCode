class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        n = len(bombs)
        graph = defaultdict(list)
        res = 1
        

        def get_island_size(root):
            q = deque([root])
            visited = set()
            visited.add(root)
            island_size = 1

            while q:
                popped = q.popleft()
                for nbor in graph[popped]:
                    if nbor in visited: continue
                    visited.add(nbor)
                    q.append(nbor)
                    island_size+=1

            return island_size


        def calc_distance(x1, y1, x2, y2):
            return sqrt((x2-x1)**2 + (y2-y1)**2)

        for i in range(n):
            for j in range(n):
                if i == n: continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                if calc_distance(x1,y1,x2,y2) <= r1:
                    graph[i].append(j)

        for node in graph.keys():
            res = max(res, get_island_size(node))

        return res
