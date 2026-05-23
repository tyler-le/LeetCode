class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        letters = set("".join(words))

        # Build graph inline
        for i in range(n - 1):
            curr = words[i]
            after = words[i + 1]
            p1, p2 = 0, 0
            found_diff = False
            while p1 < len(curr) and p2 < len(after):
                if curr[p1] != after[p2]:
                    if after[p2] not in graph[curr[p1]]:
                        graph[curr[p1]].add(after[p2])
                        indegrees[after[p2]] += 1
                    found_diff = True
                    break
                p1 += 1
                p2 += 1
            
            if not found_diff and len(curr) > len(after): return ""
                

        # Topological sort
        q = deque()
        res = []

        for letter in letters:
            if not indegrees[letter]:
                q.append(letter)

        while q:
            level_size = len(q)
            for _ in range(level_size):
                popped = q.popleft()
                res.append(popped)
                for nbor in graph[popped]:
                    indegrees[nbor] -= 1
                    if not indegrees[nbor]:
                        q.append(nbor)

        print("res:", res, "letters:", letters, "indegrees:", dict(indegrees), "graph:", {k: v for k,v in graph.items()})
        if len(res) != len(letters): return ""
        return "".join(res)