class UnionFind:
    def __init__(self):
        self.parents = [] 
        self.email_to_index = {}
        self.index_to_email = {}

    def union(self, a, b):
        self._populate(a)
        self._populate(b)

        parent_a = self.find(self.email_to_index[a])
        parent_b = self.find(self.email_to_index[b])

        self.parents[parent_b] = parent_a
    
    def find(self, x):
        if x == self.parents[x]: return x
        return self.find(self.parents[x])
    
    def _populate(self, x):
        if x not in self.email_to_index:
            self.parents.append(len(self.parents))
            self.email_to_index[x] = len(self.parents) - 1
            self.index_to_email[len(self.parents) - 1] = x
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find based on emails
        # have a hashmap (email -> name)


        # johnsmith@mail.com john_newyork@mail.com

        # john00@mail.com johnsmith@mail.com

        # mary@mail.com

        # johnnybravo@mail.com

        uf = UnionFind()
        email_to_name_map = {}

        for account in accounts:
            name, first_email, rest = account[0], account[1], account[2:]
            if first_email not in email_to_name_map:
                email_to_name_map[first_email] = name

            if not rest:
                uf.union(first_email, first_email)
            else:
                for x in rest:
                    uf.union(first_email, x)

        res = defaultdict(list)
        result = []

        for i in range(len(uf.parents)):
            parent = uf.find(i)
            child = i
            res[parent].append(child)

        for parent_index, child_indices in res.items():
            root_email = uf.index_to_email[parent_index]
            name = email_to_name_map[root_email]
            emails = sorted([uf.index_to_email[i] for i in child_indices])
            result.append([name] + emails)

        return result


            