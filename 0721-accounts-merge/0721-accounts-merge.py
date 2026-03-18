from pprint import pprint

class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        visited = set() # emails
        email_to_name_map = {}
        res = []

        for account in accounts:
            name = account[0]
            hub_email, rest = account[1], account[2:]
            if not rest:
                graph[hub_email].append(hub_email)
                email_to_name_map[hub_email] = name
            for x in rest:
                graph[hub_email].append(x)
                graph[x].append(hub_email)
                email_to_name_map[hub_email] = name
                email_to_name_map[x] = name
            
    
        def bfs(node):
            q = deque([node])
            visited.add(node)
            sublist = []

            while q:
                popped = q.popleft()
                sublist.append(popped)

                for nbor in graph[popped]:
                    if nbor in visited: continue
                    q.append(nbor)
                    visited.add(nbor)
            
            return sublist

        for k, v in graph.items():
            if k in visited: continue
            emails = bfs(k)
            entry = []
            entry.append(email_to_name_map[k])
            entry.extend(sorted(emails))

            res.append(entry)
        
        return res
        