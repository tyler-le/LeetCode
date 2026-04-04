# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # turn to graph and run bfs from target

        graph = defaultdict(list)
        res = []
        visited = set()

        def dfs(node, parent):
            nonlocal graph
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            
            if node.left: dfs(node.left, node)
            if node.right: dfs(node.right, node)
        
        dfs(root, None)
        q = deque([(target.val, 0)]) # node, distance
        visited.add(target.val)

        while q:
            popped_node, popped_dist = q.popleft()


            if popped_dist > k: return res
            if popped_dist == k: res.append(popped_node)

            for nbor in graph[popped_node]:
                if nbor in visited: continue
                visited.add(nbor)
                q.append((nbor, popped_dist + 1))
        
        return res
