class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(list)
        letters = set([x for x in "".join(words)])
        indegrees = defaultdict(int)
        q = deque()
        res = []


        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            p1, p2 = 0, 0
            found_diff = False

            while p1 < len(w1) and p2 < len(w2):
                if w1[p1] != w2[p2]:
                    graph[w1[p1]].append(w2[p2])
                    indegrees[w2[p2]]+=1
                    found_diff = True
                    break
                p1+=1
                p2+=1
            
            if not found_diff and len(w1) > len(w2): 
                return ""
        
        for letter in letters: 
            if indegrees[letter] == 0:
                q.append(letter)
                res.append(letter)

        print(graph)

        while q:
            popped = q.popleft()

            for nbor in graph[popped]:
                indegrees[nbor]-=1
                if indegrees[nbor] == 0:
                    q.append(nbor)
                    res.append(nbor)

        return "".join(res)