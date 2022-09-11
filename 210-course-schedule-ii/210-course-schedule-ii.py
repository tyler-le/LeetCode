class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        We are essentially adding to res based on in-degree of zero 
        in order to do topological sort
        '''
        
        hmap, indegree, q, res = collections.defaultdict(list), {}, deque(), []
        
        # build directed adjacency list
        # u -> v where u is a prereq of v
        for dest, src in prerequisites:
            hmap[src].append(dest)
            indegree[dest] = 1 + indegree.get(dest, 0)
        
        # build q containing nodes with indegree of zero
        for i in range (numCourses):
            if i not in indegree: q.append(i)
        
        while q:
            # visit all neighbors of current node
            curr = q.popleft()
            
            # add curr node to res since it has in-degree zero (no prereqs)
            res.append(curr)
            
            # decrement indegree of each neighbor since we cherry-picked curr out. 
            # if it ends up at zero, append to q
            for nbor in hmap[curr]:
                indegree[nbor]-=1
                if indegree[nbor] == 0: 
                    q.append(nbor)

        return res if len(res) == numCourses else []
        
        
            
            