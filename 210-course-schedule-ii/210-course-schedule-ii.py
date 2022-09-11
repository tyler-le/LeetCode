class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        We are essentially adding to res based on in-degree of zero 
        in order to do topological sort
        '''
        
        hmap, indegree, q, res = collections.defaultdict(list), {}, deque(), []
        
        # build directed adjacency list
        for dest, src in prerequisites:
            hmap[src].append(dest)
            indegree[dest] = 1 + indegree.get(dest, 0)
        
        # build q containing nodes with indegree of zero
        for i in range (numCourses):
            if i not in indegree: q.append(i)
        
        while q:
            # visit all neighbors in each node of q 
            curr = q.popleft()
            
            # add curr node to res
            res.append(curr)
            
            # decrement indegree. if zero, add to q
            for nbor in hmap[curr]:
                indegree[nbor]-=1
                if indegree[nbor] == 0: q.append(nbor)

            
        return res if len(res) == numCourses else []
        
        
            
            