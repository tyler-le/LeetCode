# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # convert binary tree to undirected graph
        graph = collections.defaultdict(list)
        
        def build_graph(curr, parent):
            if curr and parent:
                graph[curr].append(parent)
                graph[parent].append(curr)
            if curr.left:
                build_graph(curr.left, curr)
            if curr.right:
                build_graph(curr.right, curr)
                
        build_graph(root, None)

        # run bfs on target node and record dist == 2
        q = deque([(target,0)]) # (node, dist) pairs
        dist, visited, res = 0, set(), []
        
        while q:
            popped, dist = q.popleft()
            visited.add(popped)
            
            if dist == k: res.append(popped.val)

            for nbor in graph[popped]:
                if nbor not in visited:
                    q.append((nbor, dist+1))
                          
        return res
            