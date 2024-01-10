# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        
        def dfs(node):

            if node.left: 
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
                
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
                
        
        dfs(root)
        q = deque([start])
        res = -1
        visited = set([start])
        
        while q:

            level_size = len(q)
            
            for _ in range(level_size):
                popped = q.popleft()
                
                for nbor in graph[popped]:
                    if nbor not in visited:
                        q.append(nbor)
                        visited.add(nbor)
            res+=1

        return res 