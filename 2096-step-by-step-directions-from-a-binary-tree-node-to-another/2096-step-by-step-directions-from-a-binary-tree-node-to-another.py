# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        UP, LEFT, RIGHT = "U", "L", "R"
        graph = defaultdict(list) # (node, edge type)

        # Build graph with {UP, LEFT, RIGHT} edges between nodes
        def dfs(node, parent):
            nonlocal graph
            if not node: return

            if parent: 
                graph[node.val].append((parent.val, UP))

            if node.left:
                dfs(node.left, node)
                graph[node.val].append((node.left.val, LEFT))

            if node.right:
                dfs(node.right, node)
                graph[node.val].append((node.right.val, RIGHT))
        
        dfs(root, None)
        
        
        # Run BFS from Start to Dest
        q = deque([(startValue, "")]) # (node, curr_path)
        res, visited = [], set()

        while q:
            popped_node, popped_path = q.popleft()
        
            for nbor_node, nbor_edge_type in graph[popped_node]:
                if nbor_node in visited: continue
                if nbor_node == destValue: return popped_path + nbor_edge_type
                
                q.append((nbor_node, popped_path + nbor_edge_type))
                visited.add(nbor_node)